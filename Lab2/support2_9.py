from PIL import Image, ImageDraw
import math


class GraphVisual:
    def __init__(
            self,
            cnt,
            rts,
            size_coef=1,
            ratio_coef=1,
            bg_color=(182, 225, 185),
            fg_color=(0, 0, 0),
            is_naprav=False,
            vzves=False,
            gr_label="Here can be graph name"
                ):
        self.__cnt = cnt
        self.__rts = rts
        self.__Img_Width = 1000*size_coef
        self.__Img_Height = 1100*size_coef
        self.__ratio_coef = ratio_coef
        self.__bg_color = bg_color
        self.__fg_color = fg_color
        self.__is_naprav = is_naprav
        self.__vzves = vzves
        self.__gr_label = gr_label
        self.__img = Image.new("RGBA", (self.__Img_Width, self.__Img_Height), self.__bg_color)
        self.__draw_graph()
        self.__img.show()

    def __create_canvas(self):
        return Image.new("RGBA", (self.__Img_Width, self.__Img_Height), self.__bg_color)

    def __draw_graph(self):
        graco = []
        for i in range(self.__cnt):
            x = 400 * math.sin(i * 2 * math.pi / self.__cnt) + 500
            y = 400 * math.cos(i * 2 * math.pi / self.__cnt) + 600

            x = 500 + (x - 500) * self.__ratio_coef
            y = 600 + (y - 600) * self.__ratio_coef
            graco.append([x, y])

        func_var = 2 * math.pi / (8 * self.__cnt ** (1 / 3)) * self.__ratio_coef

        draw = ImageDraw.Draw(self.__img)

        for fr, tu, *ves in self.__rts:
            frx, fry = graco[fr]
            tux, tuy = graco[tu]
            draw.line(((frx, fry), (tux, tuy)), fill=(0, 0, 0), width=int(5 * self.__ratio_coef))

        # Рисуем метки (стрелки / кружки) и веса
        for route in self.__rts:
            fr, tu = route[:2]
            ves = route[2] if len(route) > 2 else None
            frx, fry = graco[fr]
            tux, tuy = graco[tu]

            if self.__is_naprav:
                x = frx + (5 / 8) * (tux - frx)
                y = fry + (5 / 8) * (tuy - fry)
            else:
                x = (frx + tux) / 2
                y = (fry + tuy) / 2

            importantcoef = math.atan2(frx - tux, fry - tuy)
            questioncoef = 30 * self.__ratio_coef
            if self.__is_naprav:
                draw.regular_polygon(
                    (x, y, questioncoef),
                    3,
                    rotation=math.degrees(importantcoef) if (fry - tuy) != 0 else 180.0,
                    fill=self.__fg_color
                )
            elif self.__vzves:
                draw.ellipse(
                    (x - questioncoef, y - questioncoef, x + questioncoef, y + questioncoef),
                    fill=self.__fg_color
                )

            if self.__vzves:
                contrast = (255 - self.__fg_color[0], 255 - self.__fg_color[1], 255 - self.__fg_color[2])
                draw.text(
                    (x, y),
                    f"{ves}",
                    fill=contrast,
                    font_size=int(questioncoef * max(1, func_var)),
                    anchor="mm"
                )

        versh_size = int(160 * func_var)
        count = 0
        for j, k in graco:
            draw.ellipse(
                (j - versh_size, k - versh_size, j + versh_size, k + versh_size),
                fill=(255, 255, 255)
            )
            draw.text(
                (j, k),
                f"{count}",
                fill=self.__fg_color,
                font_size=versh_size,
                anchor="mm"
            )
            count += 1
        draw.text(
            (0, 0),
            text=self.__gr_label,
            fill=self.__fg_color,
            font_size=int(40 * self.__Img_Width/1000)
        )