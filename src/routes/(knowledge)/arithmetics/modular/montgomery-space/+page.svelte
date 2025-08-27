<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Statement from "$lib/Stencils/Blocks/Statement.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Math from "$lib/Math/Math.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Image from "$lib/Elements/Image.svelte"
</script>

<Title title="Пространство Монтгомери"
/>

<Par>
<P>
    В модулярной арифметике основная операция &mdash; само вычисление остатка от деления числа на модуль.
    Эта операция очень дорогая &mdash; целых 15&ndash;30 тактов.
</P>
</Par>

<Par>
<P>
    Вместо работы с числами в обычном виде <Math m={`a \\bmod M`}/>, Питер Монтгомери предложил
    переходить в специальное представление &mdash; <b>представление Монтгомери</b>,
    где умножение выполняется быстрее, чем классическое модульное умножение.
</P>
<P>
    Представление Монтгомери можно построить по любому модулю <Math m={`M`}/>.
    Для этого представления надо сначала выбрать число <Math m={`R`}/>,
    которое будет взаимнопросто с <Math m={`M`}/>: <Math m={`R \\rprime M`}/>.
</P>
<P>
    Обычное число <Math m={`x`}/> преобразуется в представление Монтгомери следующим образом
</P>
<Math display m={`\\overline{x} = x \\cdot R \\bmod M`}/>

<P>
    Для того, чтобы вычислить это преобразование, понадобится выполнить ту самую дорогую операцию взятия по модулю.
    К счастью, это придётся проделать только два раза для каждого числа: чтобы перевести в пространство Монтгомери
    и чтобы перевести обратно.
    Все промежуточные вычисления выполняются без этой дорогой операции.
</P>
</Par>

<Subheading>Умножение Монтгомери</Subheading>

<Par>
<P>
    Умножение Монтгомери <Math m={`*`}/> не совпадает с обычным модульном умножением <Math m={`\\cdot`}/>.
    Для того, чтобы после умножения получилось число, которое является представлением Монтгомери
    произведения операндов, нужно дополнительно домножить на <Math m={`R^{-1}`}/>:
</P>
<Math display
      m={`\\overline{a} * \\overline{b} \\defeq \\overline{a \\cdot b}
          = (a \\cdot b) \\cdot R \\bmod M = (\\overline{a} \\cdot \\overline{b}) \\cdot R^{-1} \\bmod M`}/>
<P>
    Вся прелесть в представлении Монтгомери в том, что операцию <Math m={`x \\cdot R^{-1} \\bmod M`}/>
    можно выполнить без взятия по модулю.
    Эта операция называется <b>сокращение Монтгомери</b> (Montgomery reduction).
</P>
</Par>

<Par>
<P>
    Расширенный алгоритм Евклида позволяет найти два числа <Math m={`R^{-1}`}/> и <Math m={`M'`}/> такое, что
</P>
<Math display m={`R \\cdot R^{-1} + M \\cdot M' = 1`}/>
<P>
    Тогда можно получить способ вычисления <Math m={`x \\cdot R^{-1}`}/>
</P>
<Math display
      m={`\\align{
          x \\cdot R^{-1} &= x \\cdot R \\cdot R^{-1} / R = \\\\
          &= x \\cdot (1 - M \\cdot M') / R \\equiv \\\\
          &\\equiv (x - x \\cdot M \\cdot M' + k \\cdot R \\cdot M) / R \\pmod{M} \\equiv \\\\
          &\\equiv \\bigl( x - (x \\cdot M' - k \\cdot R) \\cdot M \\bigr) / R \\pmod{M}
          }`}/>
<P>
    Здесь <Math m={`k`}/> &mdash; любое целое число.
    Давайте выберем <Math m={`k = \\lfloor x \\cdot M' / R \\rfloor`}/>.
    Тогда <Math m={`x \\cdot M' - k \\cdot R = x \\cdot M' \\bmod R`}/>, и
</P>
<Math display m={`x \\cdot R^{-1} \\equiv (x - x \\cdot M' \\bmod R \\cdot M) / R \\pmod{M}`}/>
<P>
    Осталась небольшая проблемка: <Math m={`x/R < M`}/> и <Math m={`x \\cdot M' \\bmod R \\cdot M / R < M`}/>,
    поэтому результат вычитания находится в интервале <Math m={`(-M, M)`}/>.
    Для решения этой проблемки надо просто добавить <Math m={`M`}/> к результату, если надо.
</P>
<P>
    Получаем уже полный алгоритм усечения
</P>
</Par>

<Codeblock code={
`const int M, R
const int Mr = inverse(M, mod R)

function reduce(int x):
    int q = x * Mr % R
    int m = q * M
    int y = (x - m) / R

    if y < 0:
        return y + M
    else:
        return y`
}/>

<Par>
<P>
    Это же усечение применяется для того, чтобы перевести число из представления Монтгомери в обычное представление.
</P>
</Par>

<Subheading>Компьютерная реализация</Subheading>

<Par>
<P>
    Что у нас в итоге получилось?
    Вместо одного умножения и одного взятия по модулю мы выполняем два умножения,
    одно сложение, одно взятие по модулю и одно деление.
    Прикол в том, что мы выполняем деление не на данное нам число <Math m={`M`}/>,
    а на почти произвольное число <Math m={`R`}/>.
</P>
<P>
    Мы можем выбрать <Math m={`R`}/> удобным для себя. Например, степень двойки!
    Деление на степень двойки можно реализовать через сдвиг, а взятие по модулю реализовывать вообще не нужно,
    если подобрать правильный тип данных.
</P>
<P>
    Итого мы получаем очень эффективный и быстрый код. Здесь я взял <Math m={`R = 2^{32}`}/>.
</P>
</Par>

<Codeblock language="cpp" code={
`typedef uint32_t u32;
typedef uint64_t u64;

constexpr u32 M = 1e9 + 7;
const u32 Mr = inverse(M, 1ull << 32);

u32 reduce(const u64 x) {
    u32 q = static_cast<u32>(x) * Mr;
    u64 m = static_cast<u64>(q) * M;
    u32 y = (x - m) >> 32;
    return x - m ? y + M : y;
}`
}/>

<Par>
<P>
    Если мы можем позволить себе вернуть число в диапазоне от <Math m={`0`}/> до <Math m={`2n-2`}/>,
    то можно отказаться от последней проверки и всегда прибавлять <Math m={`M`}/>.
    В итоге получится код <Code language="cpp" c="return y + M"/> без ветвлений.
</P>
<P>
    Можно также битовый сдвиг <Code language="cpp" c=">> 32"/> выполнять раньше
    и вычислять <Math m={`\\lfloor x / R \\rfloor - \\lfloor m / R \\rfloor`}/> вместо <Math m={`(x - m) / R`}/>.
    Так делать можно, потому что первые <Math m={`32`}/> бита в <Math m={`x`}/> и <Math m={`m`}/> совпадают:
    <Math m={`m = x \\cdot M \\cdot M' \\equiv x \\pmod R`}/>.
</P>
<P>
    В нашем случае два битовых сдвига эффективнее одного.
    Причина в том, что при вычислении <Math m={`\\lfloor m / R \\rfloor`}/> мы считаем
    <Code language="cpp" c="((u64) q * n) >> 32"/>,
    а при умножении <Math m={`32`}/>-битных чисел друг на друга
    процессоры x86/x64 старшие <Math m={`32`}/> бита пишут в отдельный регистр <Code language="asm" c="edx"/>.
</P>
</Par>

<Codeblock language="cpp" code={
`u32 reduce(const u64 x) {
    u32 q = static_cast<u32>(x) * Mr;
    u32 m = (static_cast<u64>(q) * M) >> 32;
    return (x >> 32) + M - m;
}`
}/>

<Subheading>Быстрое обратное по модулю <Math m={`R`}/></Subheading>

<Par>
<P>
    Для того, чтобы инициализировать пространство Монтгомери, нам нужно вычислить <Math m={`M' = M^{-1} \\bmod R`}/>.
    Обычно это находится с помощью расширенного алгоритма Евклида.
    Но этот метод может оказаться долговатым.
</P>
<P>
    Можно использовать тот факт, что <Math m={`R`}/> &mdash; степень двойки.
    Тогда
</P>
<Math display m={`M \\cdot x \\equiv 1 \\pmod{2^k} \\implies M \\cdot x \\cdot (2 - M \\cdot x) \\equiv 1 \\pmod{2^{2k}}`}/>
<P>
    Этот факт можно использовать для нахождения <Math m={`M'`}/>.
    Начнём с <Math m={`x = 1`}/> как с обратного для <Math m={`M`}/> по модулю <Math m={`2`}/>
    и будем увеличивать степень модуля, пока не дойдем до модуля <Math m={`R`}/>.
    Нам понадобится для этого <Math m={`\\log_2 R`}/> итераций.
</P>
</Par>

<Codeblock code={
`function inverse(int M, mod int R):
    Mr = 1
    repeat log2(R) times:
        Mr *= 2 - M * Mr
    return Mr`
}/>

<Par>
<P>
    Код инициализации в C++ будет абсолютно такой же
</P>
</Par>

<Codeblock language="cpp" code={
`struct Montgomery {
    u32 M, Mr;

    constexpr explicit Montgomery(const u32 M) : M(M), Mr(1) {
        for (int i = 0; i < 5; i++)
            Mr *= 2 - M * Mr;
    }

    ...
}`
}/>


<Subheading>Быстрое обратное преобразование</Subheading>


<Heading>Сокращение Барретта</Heading>


<Heading>Деление без деления</Heading>

<Par>
<P>
    Вообще надо всегда по возможности отказываться от операций взятия по модулю.
</P>
<P>
    Банальный пример: нужно посчитать сумму чисел в массиве <Code c="a"/> по модулю <Math m={`M`}/>,
    при этом все числа массива меньше модуля <Math m={`M`}/>.
</P>
<P>
    Интуитивно понятный код может оказаться медленным. Вот наивная реализация
</P>
</Par>

<Codeblock language="c" code={
`const int M = 1000000009;

int sum(int *a, int n) {
    int s = 0;
    for (int i = 0; i < n; i++) {
        s = (s + a[i]) % M;
    }
    return s;
}`
}/>

<Par>
<P>
    Можно заметить, что раз <Math m={`\\code{a}[i] < M`}/>, и в начале каждой итерации <Math m={`s < M`}/>, то
    <Math m={`s + \\code{a}[i] < 2M`}/>, а значит операцию взятия остатка можно заменить на простое условие и вычитание
</P>
</Par>


<Codeblock language="c" code={
`const int M;
int *a, int n;

int s = 0;
for (int i = 0; i < n; i++) {
    s += a[i];
    if (s >= M) {
        s = s - M;
    }
}`
}/>
