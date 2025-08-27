<script>
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Statement from "$lib/Stencils/Blocks/Statement.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Count sketch"
/>

<Par>
    <P>
        Пусть у нас есть поток данных (stream) <Math m={`s_1, s_2, s_3, \\dotsc, s_i, \\dotsc`}/>,
        при этом все данные &mdash; элементы какого-то универсума <Math m={`\\UUU`}/>.
        Мы хотим уметь считать, сколько раз элемент <Math m={`x`}/> встретился в этом потоке к моменту времени
        <Math m={`t`}/>, то есть уметь считать значение функции
    </P>
    <Math display m={`f_t(x) = \\sum_{i=1}^t \\indic(s_i = x)`}/>

    <P>
        Будем решать задачу для фиксированной временной границы <Math m={`t`}/>.
    </P>
</Par>

<Statement title="Задача подсчета">
    <P>
        Дан поток данных <Math m={`S = s_1, s_2, s_3, \\dotsc, s_{n-1}, s_n`}/>.
        Можно считать, что мы сделали временной срез при <Math m={`t = n`}/>.
    </P>
    <P>
        Нам нужно оценивать количество вхождений элемента <Math m={`x`}/> в этот поток <Math m={`S`}/> &mdash;
        значение функции <Math m={`f(x)`}/>.
    </P>
    <Math display m={`f(x) = \\sum_{i=1}^n \\indic(s_i = x)`}/>
    <P>
        Но ответы на запросы лояльные. Мы даем ответ с точностью <Math m={`\\epsilon`}/>,
        при этом позволяем себе ошибаться с вероятностью <Math m={`\\delta`}/>.
        Формально, <Math m={`\\prob \\big( \\hat f (x) \\le f(x) + \\epsilon n \\big) \\ge 1 - \\delta`}/>,
        где <Math m={`\\hat f (x)`}/> &mdash; предсказанное нами количество вхождений.
    </P>
    <P>
        А ещё нам нужно уметь обновлять поток &mdash; добавлять и удалять элементы.
    </P>
</Statement>

<Heading>Count-Min sketch</Heading>

<Par>
    <P>
        Для решения задачи подсчета можно использовать структуру данных Count-Min sketch.
        Она применима только тогда, когда в поток элементы только добавляются.
    </P>
</Par>

<Par>
    <P>
        Будем использовать хеширование.
    </P>
    <P>
        Пусть <Math m={`d = \\lceil \\ln 1/\\delta \\rceil`}/> &mdash; глубина aka количество хеш-функций,
        и <Math m={`w = \\lceil e/\\epsilon \\rceil`}/> &mdash; размер хеш-пространства.
        Счётчики будем хранить в двумерном массиве <Math m={`c \\in \\NN_0^{d \\times w}`}/>
        высоты <Math m={`d`}/> и ширины <Math m={`w`}/>.
        Изначально массив <Math m={`c`}/> проинициализирован нулями.
    </P>
    <P>
        Создадим еще <Math m={`d`}/> независимых хеш-функций
        <Math m={`h_1, h_2, \\dotsc, h_d \\colon \\UUU \\surjto \\{1, 2, \\dotsb, w\\}`}/>.
    </P>
</Par>

<Codeblock code={
`const real delta = 0.01
const real epsilon = 0.01

const int w = ceil(e / epsilon)
const int d = ceil(ln(1 / delta))

const array h[d]

array[int] c[d][w]`
}/>

<Subheading>Обновление</Subheading>

<Par>
    <P>
        При получении запроса на добавления в &laquo;счётчик&raquo; элемента <Math m={`x`}/>
        мы для каждой строки <Math m={`i`}/> массива <Math m={`c`}/> увеличиваем значение
        соответствующего счётчика <Math m={`h_i(x)`}/> на <Math m={`1`}/>.
    </P>
</Par>

<Codeblock code={
`function add(self, element):
    for i = 0; i < d; i++:
        column = h[i](element)
        c[i][column] += 1`
}/>


<Subheading>Оценка</Subheading>

<Par>
    <P>
        Для получения оценки количества вхождений элемента <Math m={`x`}/> в поток данных нам надо посчитать минимум
        по всем счётчикам, включающим в себя этот элемент:
    </P>
    <Math display m={`\\hat f (x) = \\min_{1 \\le i \\le d} c[i][h_i(i)]`}/>
    <P>
        Все показатели счетчиков получаются завышенными, ведь у любой хеш-функции неизбежно будут коллизии.
        Когда мы берем минимум, мы выбираем наименее завышенную оценку.
    </P>
</Par>

<Proof>
    <Par>
        <P>
            <b>Доказательство</b> того, что структура работает, и работает хорошо.
        </P>
        <P>
            Начнем с доказательства завышенности оценок. Для любой строки <Math m={`i`}/> и любого элемента <Math
                m={`x`}/>
        </P>
        <Math display m={`c[i][h_i(x)] = f(x) + \\sum_{\\substack{y \\neq x \\\\ h_i(y) = h_i(x)}} f(y) \\ge f(x)`}/>
        <P>
            Хеш-функции <Math m={`h_i`}/> &laquo;хорошие&raquo;, то есть они свои входы равномерно распределяют по
            выходам.
        </P>
        <P>
            Рассмотрим произвольную строку <Math m={`i`}/>. Ошибка оценки <Math m={`\\Delta_i`}/> выражается как
        </P>
        <Math display m={`\\Delta_i = c[i][h_i(x)] - f(x) = \\sum_{\\substack{y \\neq x \\\\ h_i(y) = h_i(x)}} f(y)`}/>
        <P>
            Тогда математическое ожидание ошибки оценки
        </P>
        <Math display
              m={`\\expect \\Delta_i = \\sum_{y \\neq x} f(y) \\cdot \\prob \\big( h_i(y) \\neq h_i(x) \\big) = \\frac{n - f(x)}{w} \\le \\frac{n}{w}`}/>

        <P>
            Применим неравенство Маркова
        </P>
        <Math display m={`\\prob(\\Delta_i \\ge a) \\le \\frac{\\expect \\Delta_i}{a} \\le \\frac{n}{wa}`}/>

        <P>
            Выберем <Math m={`a = \\epsilon n`}/>, тогда мы сможем получить оценку
        </P>
        <Math display m={`\\prob(\\Delta_i \\ge \\epsilon n) \\le \\frac{1}{w \\epsilon} \\le \\frac{1}{e}`}/>

        <P>
            Но это только для одной строки. А при получении оценки мы выбираем минимум, значит, общая ошибка
            превысит <Math m={`\\epsilon n`}/>, только тогда, когда переоценку дадут все <Math m={`d`}/> строк.
        </P>
        <Math display
              m={`\\prob \\Bigg( \\bigunion_{i=1}^d \\{ \\Delta_i \\ge \\epsilon n \\} \\Bigg) \\le \\left( \\frac{1}{e} \\right)^d`}/>

        <P>
            Учитывая, что <Math m={`(1/e)^d \\le e^{-\\ln 1/\\delta} = \\delta`}/>, получаем оценку
        </P>
        <Math display m={`\\prob (\\hat f (x) > f(x) + \\epsilon n ) \\le \\delta`}/>
    </Par>
</Proof>