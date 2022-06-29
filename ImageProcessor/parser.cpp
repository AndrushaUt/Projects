#include "parser.h"

void Parser::AddPositionalArg(const std::string &arg_name, Parser::Argument output) {
    positional_args_.push_back({arg_name, output});
}

void Parser::AddKeywordArg(const std::string &keyword, const std::vector<std::pair<std::string, Argument>> args) {
    keyword_fields_[keyword] = args;
}

void Parser::Parse(size_t argc, char **argv) {
    if (argc == 1) {
        throw Exception::EmptyLine;
    } else if (argc == 2) {
        throw Exception::NoOutputFile;
    }
    for (size_t i = 0; i < positional_args_.size(); ++i) {
        Internal assign(argv[i + 1]);
        std::visit(assign, positional_args_[i].second);
        size_t size = (get<std::string *>(positional_args_[i].second))->size();
        if (size < 5 or get<std::string *>(positional_args_[i].second)->substr(size - 4, size) != ".bmp") {
            if (i == 0) {
                throw Exception::WrongInputFile;
            } else if (i == 1) {
                throw Exception::WrongOutputFile;
            }
        }
    }

    for (size_t i = positional_args_.size() + 1; i < argc; ++i) {
        auto it = keyword_fields_.find(argv[i]);
        if (it == keyword_fields_.end()) {
            throw Exception::InvalidFilter;
        }
        filters_to_make_.push_back(argv[i]);
        auto param_required = it->second.size();
        for (size_t j = 1; j <= param_required; ++j) {
            if (i + j >= argc) {
                throw Exception::InvalidAmountOfArguments;
            }
            try {
                Internal assign(argv[i + j]);
                std::visit(assign, it->second[j - 1].second);
            } catch (std::invalid_argument) {
                throw Exception::InvalidTypeOfArgument;
            }
        }
        if (i + param_required + 1 < argc &&
            keyword_fields_.find(argv[i + param_required + 1]) == keyword_fields_.end()) {
            throw Exception::InvalidAmountOfArguments;
        }
        i += param_required;
    }
}

std::vector<std::string> &Parser::GetFiltersToUse() {
    return filters_to_make_;
}

void Parser::Setting(Bmp &image) {
    AddPositionalArg("input_file", &image.bh.input_file);
    AddPositionalArg("output_file", &image.bh.output_file);
    AddKeywordArg("-crop", {{"width",  &crop_params.width},
                            {"height", &crop_params.height}});
    AddKeywordArg("-blur", {{"sigma", &blur_params.sigma}});
    AddKeywordArg("-gs", {});
    AddKeywordArg("-edge", {{"threshold", &edge_params.threshold}});
    AddKeywordArg("-sharp", {});
    AddKeywordArg("-neg", {});
    AddKeywordArg("-Andrusha", {});
    AddKeywordArg("-mirror",{{"dir",&mirrorParams.dir}});
}

Parser::Internal::Internal(const char *data) : data_(data) {
}

void Parser::Internal::operator()(std::string *s) {
    *s = std::string(data_);
}

void Parser::Internal::operator()(size_t *s) {
    *s = std::stoi(data_);
}

void Parser::Internal::operator()(double *s) {
    *s = std::stod(data_);
}

