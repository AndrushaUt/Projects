#pragma once

#include <vector>
#include <variant>
#include <unordered_map>
#include <string>
#include "blur_parameters.h"
#include "crop_parameters.h"
#include "edgedetection_parameters.h"
#include "MirrorParams.h"
#include "image.h"

class Parser {
public:
    using Argument = std::variant<std::string *, double *, size_t *>;

    Parser() = default;

    void AddPositionalArg(const std::string &arg_name, Argument output);

    void AddKeywordArg(const std::string &keyword, const std::vector<std::pair<std::string, Argument>> args);

    void Parse(size_t argc, char **argv);

    std::vector<std::string> &GetFiltersToUse();

    void Setting(Bmp &image);

    struct Internal {
        Internal(const char *data);

        void operator()(std::string *s);

        void operator()(size_t *s);

        void operator()(double *s);

    private:
        const char *data_;
    };

    CropParams crop_params;
    GaussianBlurParams blur_params;
    EdgeDetectionParams edge_params;
    MirrorParams mirrorParams;
private:
    std::vector<std::pair<std::string, Argument>> positional_args_;
    std::unordered_map<std::string, std::vector<std::pair<std::string, Argument>>> keyword_fields_;
    std::vector<std::string> filters_to_make_;
};