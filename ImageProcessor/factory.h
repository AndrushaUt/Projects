#include "basefilter.h"

class Factory {
public:
    void Registration(Parser &parser);

    void Register(std::string_view name, std::function<std::unique_ptr<BaseFilter>()> creator);

    std::unique_ptr<BaseFilter> Create(std::string_view name);

private:
    std::unordered_map<std::string_view, std::function<std::unique_ptr<BaseFilter>()> > name_to_func_;
};