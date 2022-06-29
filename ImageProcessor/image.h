#include <vector>
#include <string>
#include "exception.h"
#include "color.h"
#include "bmpholder.h"

class Bmp {
public:
    Bmp() = default;

    void Read(const std::string &path, BmpHolder &bmp_holder);

    void Write(const std::string &output, BmpHolder &bmp_holder);

    BmpHolder bh;
};
