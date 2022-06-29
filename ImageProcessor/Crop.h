#include "Negative.h"

class Crop : public BaseFilter {
public:
    Crop(const CropParams &crop);

    static std::unique_ptr<BaseFilter> CreateCrop(CropParams &crop);

    void ApplyFilter(BmpHolder &image) override;

private:
    const CropParams &params_;
};