#include "Crop.h"

class Grayscale : public BaseFilter {
public:
    Grayscale() = default;

    static std::unique_ptr<BaseFilter> CreateGrayscale();

    void ApplyFilter(BmpHolder &image) override;
};