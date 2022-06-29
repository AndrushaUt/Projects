#include "EdgeDetection.h"

EdgeDetection::EdgeDetection(const EdgeDetectionParams &param) : params_(param){
}

std::unique_ptr<BaseFilter> EdgeDetection::CreateEdgeDetection(const EdgeDetectionParams &param) {
    return std::unique_ptr<BaseFilter>(new EdgeDetection(param));
}

void EdgeDetection::ApplyFilter(BmpHolder &image) {
    Grayscale gs;
    gs.ApplyFilter(image);
    MakeFilterWithMatrix(image,matrix_of_filter_);
    for (size_t i = 0; i < static_cast<size_t>(image.height); i++) {
        for (size_t j = 0; j < static_cast<size_t>(image.width); j++) {
            if (image.colors[i][j] > params_.threshold) {
                image.colors[i][j].SetColor(1);
            } else {
                image.colors[i][j].SetColor(0);
            }
        }
    }
}


