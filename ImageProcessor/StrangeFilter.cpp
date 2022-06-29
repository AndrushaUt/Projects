#include "StrangeFilter.h"

std::unique_ptr<BaseFilter> StrangeFilter::CreateAndrushaFilter() {
    return std::unique_ptr<BaseFilter>(new StrangeFilter());
}

void StrangeFilter::ApplyFilter(BmpHolder& image) {
    for (int i = 0; i < image.height; i++) {
        for (int j = 0; j < image.width / 2; j++) {
            std::swap(image.colors[i][image.width - j - 1], image.colors[i][j]);
            auto temp_save = image.colors[i][image.width - j - 1].red;
            image.colors[i][image.width - j - 1].red = image.colors[i][j].blue;
            image.colors[i][image.width - j - 1].blue = image.colors[i][j].green;
            image.colors[i][image.width - j - 1].green = temp_save;
        }
    }
}
