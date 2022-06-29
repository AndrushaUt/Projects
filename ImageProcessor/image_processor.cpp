#include "factory.h"

int main(int argc, char **argv) {
    Factory fact;
    Parser parser;
    Bmp image;
    parser.Setting(image);
    try {
        parser.Parse(argc, argv);
        image.Read(image.bh.input_file, image.bh);
        fact.Registration(parser);
        for (const auto &t: parser.GetFiltersToUse()) {
            auto obj = fact.Create(t);
            obj->ApplyFilter(image.bh);
        }
        image.Write(image.bh.output_file, image.bh);
    } catch (const Exception& exception) {
        std::cout << Message::ExceptMessage(exception) << std::endl;
    } catch(std::exception) {
        std::cout << "Возникли какие-то проблемы" << std::endl;
    }
    return 0;
}