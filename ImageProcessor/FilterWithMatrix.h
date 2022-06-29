#include "basefilter.h"

class FilterWithMatrix : public BaseFilter {
public:
    FilterWithMatrix() = default;
    virtual void ApplyFilter(BmpHolder &image) = 0;
    void MakeFilterWithMatrix(BmpHolder &image, const std::vector<std::vector<double>> &matrix);
};
