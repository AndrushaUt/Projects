#include "MirrorFilter.h"
#include "factory.h"

void Factory::Registration(Parser &parser) {
    auto new_edge_create = std::bind(EdgeDetection::CreateEdgeDetection,parser.edge_params);
    Register("-edge", new_edge_create);
    auto new_negative_create = std::bind(Negative::CreateNegative);
    Register("-neg", new_negative_create);
    auto new_sharpening_create = std::bind(Sharpening::CreateSharpening);
    Register("-sharp", new_sharpening_create);
    auto new_gray_scale_create = std::bind(Grayscale::CreateGrayscale);
    Register("-gs", new_gray_scale_create);
    auto new_crop_create = std::bind(Crop::CreateCrop,parser.crop_params);
    Register("-crop", new_crop_create);
    auto new_gaus_blur_create = std::bind(GaussianBlur::CreateGaussianBlur, parser.blur_params);
    Register("-blur", new_gaus_blur_create);
    auto new_andrusha_create = std::bind(StrangeFilter::CreateAndrushaFilter);
    Register("-Andrusha", new_andrusha_create);
    auto new_mirror_create = std::bind(MirrorFilter::CreateMirror, parser.mirrorParams);
    Register("-mirror", new_mirror_create);
}

void Factory::Register(std::string_view name, std::function<std::unique_ptr<BaseFilter>()> creator) {
    name_to_func_[name] = creator;
}

std::unique_ptr<BaseFilter> Factory::Create(std::string_view name) {
    return name_to_func_[name]();
}
