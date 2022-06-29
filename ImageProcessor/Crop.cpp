#include "Crop.h"

Crop::Crop(const CropParams &crop) : params_{crop} {
}

std::unique_ptr<BaseFilter> Crop::CreateCrop(CropParams &crop) {
    return std::unique_ptr<BaseFilter>(new Crop(crop));
}

void Crop::ApplyFilter(BmpHolder &image) {
    int bits[] = {0, 8, 16, 24};
    if (params_.width < static_cast<size_t>(image.width)) {
        image.width = params_.width;
        for (size_t i = 4; i <= 7; i++) {
            image.information_header[i] = static_cast<unsigned char>(params_.width >> bits[i - 4]);
        }
    }
    if (params_.height < static_cast<size_t>(image.height)) {
        size_t j = 0;
        for (size_t i = image.height - params_.height; i < static_cast<size_t>(image.height); i++) {
            std::swap(image.colors[j], image.colors[i]);
            ++j;
        }
        image.height = params_.height;
        for (size_t i = 8; i <= 11; i++) {
            image.information_header[i] = static_cast<unsigned char>(params_.height >> bits[i - 8]);
        }
    }
    image.file_size =
            SIZE_OF_INFO_HEADER + SIZE_OF_BMP_HEADER + image.height * image.width * 3 +
            ((4 - (image.width * 3) % 4) % 4) * image.height;
    for (size_t i = 2; i <= 5; i++) {
        image.file_header[i] = static_cast<unsigned char>(image.file_size >> bits[i - 2]);
    }
}

