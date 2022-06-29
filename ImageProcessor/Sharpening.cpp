#include "Sharpening.h"

std::unique_ptr<BaseFilter> Sharpening::CreateSharpening() {
    return std::unique_ptr<BaseFilter>(new Sharpening());
}

void Sharpening::ApplyFilter(BmpHolder &image) {
    MakeFilterWithMatrix(image,matrix_of_filter_);
}


