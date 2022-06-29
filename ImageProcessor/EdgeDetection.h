#include "Sharpening.h"

class EdgeDetection : public FilterWithMatrix{
public:
    EdgeDetection(const EdgeDetectionParams &param);

    static std::unique_ptr<BaseFilter> CreateEdgeDetection(const EdgeDetectionParams &param);

    void ApplyFilter(BmpHolder &image) override;

private:
    const std::vector<std::vector<double>> matrix_of_filter_ = {{0.,  -1., 0.},
                                                                {-1., 4.,  -1.},
                                                                {0.,  -1., 0.}};
    const EdgeDetectionParams &params_;
};