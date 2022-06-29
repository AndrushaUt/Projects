#include "Negative.h"

std::unique_ptr<BaseFilter> Negative::CreateNegative() {
    return std::unique_ptr<BaseFilter>(new Negative());
}

void Negative::ApplyFilter(BmpHolder &image) {
    for (size_t i = 0; i < static_cast<size_t>(image.height); i++) {
        for (size_t j = 0; j < static_cast<size_t>(image.width); j++) {
            image.colors[i][j].red = 1 - image.colors[i][j].red;
            image.colors[i][j].green = 1 - image.colors[i][j].green;
            image.colors[i][j].blue = 1 - image.colors[i][j].blue;
        }
    }
}
