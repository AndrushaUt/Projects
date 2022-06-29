#include "FilterWithMatrix.h"

void FilterWithMatrix::MakeFilterWithMatrix(BmpHolder &image, const std::vector<std::vector<double>> &matrix) {
    std::vector<std::vector<Color>> new_colors;
    new_colors.resize(image.height);
    for (size_t i = 0; i < static_cast<size_t>(image.height); i++) {
        new_colors[i].resize(image.width);
    }
    for (int i = 0; i < image.height; i++) {
        for (int j = 0; j < image.width; j++) {
            Color sum;
            for (int w = -(matrix[0].size()/2); w <= static_cast<int>((matrix[0].size()/2)); w++) {
                for (int z = -(matrix.size()/2); z <= static_cast<int>((matrix.size()/2)); z++) {
                    if (0 <= i + z and i + z < image.height and 0 <= j + w and j + w < image.width) {
                        sum += (image.colors[i + z][j + w] * matrix[z + 1][w + 1]);
                    } else {
                        int new_coord_x = 0;
                        int new_coord_y = 0;
                        if (i + z < 0) {
                            new_coord_y = 1;
                        } else if (i + z >= image.height) {
                            new_coord_y = -1;
                        }
                        if (j + w < 0) {
                            new_coord_x = 1;
                        } else if (j + w >= image.width) {
                            new_coord_x = -1;
                        }
                        sum += (image.colors[i + z + new_coord_y][j + w + new_coord_x]) *
                               matrix[z + 1][w + 1];
                    }
                }
            }
            new_colors[i][j].SetColorMax(0.,sum);
            new_colors[i][j].SetColorMin(1.);
        }
    }
    image.colors = new_colors;
}
