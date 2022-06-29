#include "StrangeFilter.h"

class MirrorFilter: public BaseFilter {
public:
    MirrorFilter(const MirrorParams& params);
    void ApplyFilter(BmpHolder& image) override;
    static std::unique_ptr<BaseFilter> CreateMirror(const MirrorParams &mr);
private:
    const MirrorParams params_;
};


