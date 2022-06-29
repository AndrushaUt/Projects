#include "basefilter.h"

class Negative : public BaseFilter {
public:
    Negative() = default;

    static std::unique_ptr<BaseFilter> CreateNegative();

    void ApplyFilter(BmpHolder &image) override;
};