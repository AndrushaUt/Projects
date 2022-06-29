#include "EdgeDetection.h"

class GaussianBlur : public BaseFilter {
public:
    GaussianBlur(const GaussianBlurParams &gs);

    static std::unique_ptr<BaseFilter> CreateGaussianBlur(const GaussianBlurParams &gs);

    void ApplyFilter(BmpHolder &image) override;

private:
    const GaussianBlurParams &params_;
};