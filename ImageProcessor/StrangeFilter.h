#include "GaussianBlur.h"

class StrangeFilter : public BaseFilter {
public:
    StrangeFilter() = default;

    static std::unique_ptr<BaseFilter> CreateAndrushaFilter();

    void ApplyFilter(BmpHolder& image) override;
};