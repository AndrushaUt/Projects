struct Color {
    double red = 0.0;
    double green = 0.0;
    double blue = 0.0;

    Color operator*(double num) const;

    Color &operator+=(const Color &other);

    Color &operator*=(const Color &other);

    Color &operator*=(double num);

    bool operator>(double num) const;

    bool operator==(double num) const;

    void SetColor(double num);

    void SetColorMin(double num);

    void SetColorMax(double num, const Color& other);

};