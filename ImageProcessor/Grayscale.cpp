#include "Grayscale.h"

std::unique_ptr<BaseFilter> Grayscale::CreateGrayscale() {
    return std::unique_ptr<BaseFilter>(new Grayscale());
}

void Grayscale::ApplyFilter(BmpHolder &image) {
    for (size_t i = 0; i < static_cast<size_t>(image.height); i++) {
        for (size_t j = 0; j < static_cast<size_t>(image.width); j++) {
            auto color = 0.299 * image.colors[i][j].red + 0.587 * image.colors[i][j].green +
                         0.114 * image.colors[i][j].blue;
            image.colors[i][j].SetColor(color);
        }
    }
}
