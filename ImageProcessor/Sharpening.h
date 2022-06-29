#include "Grayscale.h"
#include "FilterWithMatrix.h"

class Sharpening : public FilterWithMatrix {
public:
    Sharpening() = default;

    static std::unique_ptr<BaseFilter> CreateSharpening();

    void ApplyFilter(BmpHolder &image) override;

private:
    const std::vector<std::vector<double>> matrix_of_filter_ = {{0.,  -1., 0.},
                                                                {-1., 5.,  -1.},
                                                                {0.,  -1., 0.}};
};