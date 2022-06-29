#include "GaussianBlur.h"

GaussianBlur::GaussianBlur(const GaussianBlurParams &gs) : params_{gs} {
}

std::unique_ptr<BaseFilter> GaussianBlur::CreateGaussianBlur(const GaussianBlurParams &gs) {
    return std::unique_ptr<BaseFilter>(new GaussianBlur(gs));
}

void GaussianBlur::ApplyFilter(BmpHolder &image) {
    std::vector<std::vector<Color>> new_colors;
    new_colors.resize(image.height);
    for (size_t i = 0; i < static_cast<size_t>(image.height); i++) {
        new_colors[i].resize(image.width);
    }
    std::vector<double> exp_vec;
    for (size_t i = 0; i < static_cast<size_t>(std::max(image.height, image.width)); i++) {
        exp_vec.push_back(std::pow(M_E, -(std::pow(i, 2)) / (2 * std::pow(params_.sigma, 2))) /
                          (std::sqrt(2 * M_PI * std::pow(params_.sigma, 2))));
    }
    for (int i = 0; i < image.height; i++) {
        for (int j = 0; j < image.width; j++) {
            for (int z = 0; z < image.height; z++) {
                new_colors[i][j] += image.colors[z][j] * exp_vec[std::abs(i - z)];
                if (new_colors[i][j] == 1. or new_colors[i][j] > 1.) {
                    new_colors[i][j].SetColorMin(1.);
                    break;
                }
            }
        }
    }
    image.colors = new_colors;
    for (int i = 0; i < image.height; i++) {
        for (int j = 0; j < image.width; j++) {
            new_colors[i][j].SetColor(0);
            for (int z = 0; z < image.width; z++) {
                new_colors[i][j] += image.colors[i][z] * exp_vec[std::abs(j - z)];
                if (new_colors[i][j] == 1. or new_colors[i][j] > 1.) {
                    new_colors[i][j].SetColorMin(1.);
                    break;
                }
            }
        }
    }
    image.colors = new_colors;
}

