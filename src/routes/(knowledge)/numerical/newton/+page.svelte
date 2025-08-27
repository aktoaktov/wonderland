<script>
    import Heading from "$lib/Markup/Heading.svelte"
    import Statement from "$lib/Stencils/Blocks/Statement.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Par from "$lib/Markup/Par.svelte"
</script>


<Statement title="Нахождение корня функции">
    <P>
        Пусть <Math m={`f \\colon \\RR \\to \\RR`}/>.
        Мы хотим найти корень <Math m={`f`}/>, то есть такую точку <Math m={`x^* \\in \\RR`}/>, что
    </P>
    <Math display m={`f(x^*) = 0`}/>
</Statement>


<Heading>Скалярная функция многих переменных</Heading>

<Statement title="Нахождение корня скалярной функции многих переменных">
    <P>
        Пусть <Math m={`f \\colon \\RR^n \\to \\RR`}/>.
        Мы хотим найти корень <Math m={`f`}/>, то есть такой вектор <Math m={`x^* \\in \\RR^n`}/>, что
    </P>
    <Math display m={`f(x^*) = 0`}/>
</Statement>


<P>
    Будем опять находить решение итеративно.
    Пусть <Math m={`x_k`}/> &mdash; какое-то приближённое решение задачи, и мы хотим улучшить это решение.
    То есть мы хотим найти такое <Math m={`\\Delta x`}/>, чтобы <Math m={`f(x_k + \\Delta x) = 0`}/>.
</P>

<P>
    По формуле Тейлора
</P>
<Math display m={`f(x_k + \\Delta x) \\approx f(x_k) + \\nabla f (x_k) ^\\T \\cdot \\Delta x`}/>

<P>
    Мы очень хотим выбрать такой шаг <Math m={`\\Delta x`}/>, чтобы <Math m={`f(x_k + \\Delta x) = 0`}/>.
    Используем предыдущую формулу
</P>

<Math display m={`f(x_k) + \\nabla f (x_k) ^\\T \\cdot \\Delta x \\approx 0`}/>

<P>
    Теперь нам нужно выбрать вектор <Math m={`\\Delta x`}/>, по которому нужно двигаться.
    Учитывая, что градиент &mdash; направление наибыстрейшего подъема, кажется естественным выбрать вектор
    <Math m={`\\Delta x`}/> так, чтобы он был коллинеарен градиенту
</P>

<Math display m={`\\Delta x = - \\alpha \\cdot \\nabla f (x_k)`}/>

<P>
    Осталось решить уравнение <Math m={`f(x_k) + \\nabla f (x_k) ^\\T \\cdot (- \\alpha \\cdot \\nabla f (x_k)) = 0`}/>.
    Получаем
</P>

<Math display
      m={`\\alpha = \\frac{f(x_k)}{\\nabla f (x_k) \\cdot \\nabla f (x_k) ^\\T} = \\frac{f(x_k)}{ \\|\\nabla f (x_k)\\|_2^2}`}/>

<P>
    Мы поняли, как выбирать шаг, для того чтобы двигаться к нулю все ближе.
    Результирующий алгоритм состоит всего из одной формулы
</P>

<Math display m={`x_{k+1} = x_k - \\frac{f(x_k)}{\\| \\nabla f (x_k) \\|_2^2} \\cdot \\nabla f (x_k)`}/>

<P>
    Напишем алгоритм в псевдокоде.
    Для этого нам нужно уметь вычислять функцию <Math m={`f`}/> и её градиент <Math m={`\\nabla f`}/>.
</P>

<Codeblock code={
`function f(vector x) -> real: ...
function gradient(vector[real] x) -> vector[real]: ...

function solve_by_newton(f, gradient) -> real:
    select x: real

    while f(x) >= EPSILON:
        x = f(x) / (norm(gradient(x)) ** 2) * gradient(x)`}
/>

<Subheading>Далёкие от корня значения</Subheading>

<Par>
    <P>
        Наш метод будет работать только если начальное значение <Math m={`x_0`}/> уже близко к корню.
        Если это не так, то у нас точно возникнет большое количество проблем.
    </P>
    <P>
        Вместо поиска корня <Math m={`f`}/> можно найти минимум функции <Math m={`\\frac{1}{2} f(x)^2`}/>.
        В принципе, для этого можно использовать и другие алгоритмы, но мы посмотрим на алгоритм Ньютона.
    </P>

    <Math display m={`\\nabla \\left( \\frac{1}{2} \\cdot f^2 \\right) = f \\cdot \\nabla f \\quad\\text{и}\\quad
    \\hess \\left( \\frac{1}{2} \\cdot f^2 \\right) = \\nabla f \\cdot \\nabla f ^\\T + f \\cdot \\hess f`}/>

    <P>
    </P>
</Par>