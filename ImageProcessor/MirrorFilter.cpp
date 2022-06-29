#include "MirrorFilter.h"

MirrorFilter::MirrorFilter(const MirrorParams &params):params_(params) {
}

void MirrorFilter::ApplyFilter(BmpHolder &image) {
    if (params_.dir == "v"){
        for (int y = 0; y < image.height; ++y){
            for (int x = 0; x < image.width / 2; ++x){
                std::swap(image.colors[y][x], image.colors[y][image.width - 1 - x]);
            }
        }
    } else if (params_.dir == "h"){
        for (int x = 0; x < image.height / 2; ++x){
            std::swap(image.colors[x], image.colors[image.height - 1 - x]);
        }
    } else{
        throw Exception::InvalidArgument;
    }
}

std::unique_ptr<BaseFilter> MirrorFilter::CreateMirror(const MirrorParams &mr) {
    return std::unique_ptr<BaseFilter>(new MirrorFilter(mr));
}
