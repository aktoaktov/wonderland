<script>
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Math from "$lib/Math/Math.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Image from "$lib/Elements/Image.svelte"

    import metricBallsImage from "./metric-balls.svg"
</script>

<Title title="Метрические пространства"
/>

<section>
<Par>
<P>
    <b>Метрика</b> на множестве <Math m="X"/> &mdash; функция расстояния <Math m="d \colon X \times X \to \RR"/>,
    обладающая
    свойствами
</P>
<EnumList>
    <ListItem><Math m="d(x, y) \ge 0"/> и <Math m="d(x, y) = 0 \Harr x = y"/></ListItem>
    <ListItem><Math m="d(x, y) = d(y, x)"/> &mdash; симметричность</ListItem>
    <ListItem><Math m="d(x, y) \le d(x, z) + d(y, z)"/> &mdash; неравенство треугольника</ListItem>
</EnumList>
</Par>

<Par>
<P>Метрика на <Math m="X"/> &mdash; способ мерить расстояния между точками множества <Math m="X"/>.</P>
</Par>

<Par title="Метрическое пространство">
<P>
    <b>Метрическое пространство</b>
    <Math m="(X, d)"/> &mdash; множество <Math m="X"/>, снабженное
    метрикой <Math m="d \colon X \times X \to \RR"/>.
</P>
</Par>

<Par>
<P>
    Например, <Math m="\RR"/> вместе со стандартной метрикой <Math m="d(x, y) = |x - y|"/> является метрическим
    пространством.
</P>
<P>
    На основе этой метрике можно построить другие метрики на <Math m="\RR"/>.
</P>
<P>
    Пусть <Math m="f \colon [0, +\infty) \to \RR"/> &mdash; строго выпуклая неотрицательная функция, равная нулю
    только при
    <Math m="x = 0"/>. Тогда функция <Math m="d(x, y) = f \big( |x-y| \big)"/> является метрикой на <Math m="\RR"/>.
</P>
</Par>

<Par>
<P>
    Пусть теперь мы в <Math m="\RR^n"/>. Будем мерить расстояние между
    точками <Math m="x = (x_1, x_2, \dotsc, x_n)"/> и <Math m="y = (y_1, y_2, \dotsc, y_n)"/>.
</P>
<P>
    Стандартная Евклидова метрика на <Math m="\RR^n"/> определяется как
</P>
<Math display m={`d(x, y) = \\sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + \\dotsb + (x_n - y_n)^2}`}/>
<P>
    Эту метрику можно обобщить до <Math m="p"/>-метрики Гёльдера
</P>
<Math display
      m={`d(x, y) = \\sqrt[p]{ |x_1 - y_1|^p + |x_2 - y_2|^p + \\dotsb + |x_n - y_n|^p } \\quad \\text{где}~p \\ge 1`}/>
<P>
    Устремив в этой метрике <Math m="p"/> к бесконечности мы получим <Math m="\max"/>-метрику
</P>
<Math display m={`d(x, y) = \\max \\big\\{ |x_1 - y_1|, |x_2 - y_2|, \\dotsc, |x_n - y_n| \\big\\}`}/>

<P>Еще одна широко используемая метрика &mdash; метрика Минковского</P>
<Math display m={`d(x, y) = |x_1 - y_1| + |x_2 + y_2| + \\dotsb + |x_n - y_n|`}/>
</Par>

<Par>
<P>
    Пространство может быть и дискретным. Например, возьмем две битовые строки <Math m={`a, b \\in \\{0, 1\\}^n`}/>
    и посмотрим на количество различных битов. Мы задали метрику
</P>
<Math display m={`d(a, b) = \\sum_{i=1}^n \\, [a_i \\neq b_i]`}/>
</Par>

<Par>
<P>Тривиальным примером является метрика, задающая дискретную топологию. При неё все точки пространства находятся
    друг от друга на расстоянии <Math m="1"/></P>
<Math display m={`d(x, y) = [x != y]`}/>
</Par>


<Heading>Открытые и замкнутые подмножества</Heading>

<Par>
<P>
    Пусть <Math m="(X, d)"/> &mdash; метрическое пространство. Подобно тому, как мы делали в <Math m="\RR"/> и <Math
        m="\RR^n"/>, можно ввести на <Math m="(X, d)"/> понятие шаров и окрестностей точек.
</P>
</Par>

<Par title="Шар">
<P><b>Шар</b> с центром в точке <Math m="a \in X"/> и радиусом <Math m="\delta > 0"/> &mdash; множество</P>
<Math display m={`B(a, \\delta) \\defeq \\{ x \\in X : d(a, x) < \\delta \\}`}/>
<P>Шар <Math m="B(a, \delta)"/> еще называется <Math m="\delta"/>-окрестностью точки <Math m="a"/>.</P>
</Par>

<Par>
<P>
    Посмотрим на то, как выглядят шары в <Math m="\RR^2"/> при разных метриках
</P>
<Image src={metricBallsImage} alt="Шары в метрических пространствах"/>
<P>Шары могут иметь совсем уж противоестественную форму, так что буквально понимать слово &laquo;шар&raquo; не
    надо.</P>
</Par>

<Par title="Открытое множество">
<P>
    Множество <Math m="G \subset X"/> называется <b>открытым</b>, если вместе с любой своей точкой оно содержит её
    окрестность.
</P>
<Math display m="x \in G \implies \exists \delta > 0 \colon B(x, \delta) \subset G"/>
</Par>

<Par>
<P>
    Всё пространство <Math m="X"/> и пустое множество <Math m="\nothing"/> являются открытыми множествами.
    Также любой шар <Math m="B(a, \delta)"/> и его внешность <Math m={`\\{ x \\in X : d(a, x) > \\delta \\}`}/>
    &mdash;
    открытые множества.
</P>
</Par>

<Par title="Замкнутое множество">
<P>
    Множество <Math m="G"/> называется <b>замкнутым</b>, если его дополнение <Math m="X \without G"/> открыто.
</P>
</Par>

<Par>
<P>
    Аналогично обычному открытому шару, можем определить <b>замкнутый шар</b>
</P>
<Math display m={`\\widetilde{B} (a, \\delta) \\defeq \\{x \\in X : d(a, x) \\le \\delta \\}`}/>
</Par>

<Par>
<P>
    Объединение открытых множеств открыто, и пересечение конечного числа открытых множеств открыто.
</P>
<P>
    Пересечение замкнутых множеств замкнуто, и объединение конечного числа замкнутых множеств замкнуто.
</P>
</Par>


<Par>
<P>
    <b>Окрестностью</b> точки называется открытое множество, содержащее эту точку.
</P>
</Par>

<Par title="Внутренние, внешние и граничные точки">
<P>
    Точка <Math m="x \in X"/> по отношению к множеству <Math m="E \subset X"/> называется
</P>
<BulletList wide>
    <ListItem>
        <b>внутренней</b> точкой <Math m="E"/>, если она содержится в <Math m="E"/> вместе с какой-то своей
        окрестностью
    </ListItem>
    <ListItem>
        <b>внешней</b> точкой <Math m="E"/>, если она является внутренней точкой дополнения <Math m="X \without E"/>
    </ListItem>
    <ListItem>
        <b>граничной</b> точкой <Math m="E"/>, если она не является ни внутренней, ни внешней, то есть если в любой
        окрестности этой точки имеются как точки из <Math m="E"/>, так точки из <Math m="X \without E"/>
    </ListItem>
</BulletList>
</Par>

<Par>
<P>
    Например, у множества <Math m="[1, 2] \subset \RR"/>
    внутренними являются все точки из <Math m="(1, 2)"/>,
    а внешними из <Math m="(-\infty, 1) \union (2, +\infty)"/>.
</P>
<P>
    Для шара <Math m="B(a, r)"/> множество граничных точек &mdash; сфера <Math m={`\\{ x \\in X : d(a, x = r) \\}`}/>
</P>
</Par>

<Par>
<P>
    <b>Внутренность</b> множества <Math m="E"/> &mdash; множество всех внутренних точек <Math m="E"/>
</P>
<Math display m={`\\interior E \\defeq \\{x \\in X : x ~\\text{является внутренней точкой}~ E \\}`}/>

<P>
    <b>Граница</b> множества <Math m="E"/> &mdash; множество всех граничных точек <Math m="E"/>
</P>
<Math display m={`\\boundary E \\defeq \\{x \\in X : x ~\\text{является граничной точкой}~ E \\}`}/>

</Par>

<Heading>Построение метрик</Heading>


<Par>
<P>Примеры метрических пространств</P>
<BulletList wide>
    <ListItem>
        Евклидово пространство <Math m="\EE^n = (\RR^n, d_e)"/>, <br/>
        где <Math m={`d_e (x, y) = \\sqrt{(x_1-y_1)^2 + \\cdots + (x_n-y_n)^2}`}/>
        &mdash; евклидова метрика.
    </ListItem>
    <ListItem>Дискретная топология, где <Math m="X"/> &mdash; любое, а <Math m="d(x, y) = [x != y]"/></ListItem>

    <ListItem>
        Пространство <Math m="C[a,b]"/>, <br/>
        <Math m="X"/> &mdash; все непрерывные на <Math m="[a, b]"/> функции,
        и <Math m="d(f, g) = \max_x |f(x) - g(x)|"/>.
    </ListItem>

    <ListItem>
        Пространство <Math m="C^k[a,b]"/>,
        <Math m="X"/> &mdash; все <Math m="k"/> раз дифференцируемые на <Math m="[a, b]"/> функции,<br/>
        и <Math
            m={`d(f, g) = \\max \\bigl|f(x) - g(x)\\bigr| + \\max \\bigl|f'(x) - g'(x)\\bigr| + \\cdots + \\max \\bigl|f^{(k)}(x) - g^{(k)}(x)\\bigr|`}/>.
    </ListItem>

    <ListItem>
        Пространство <Math m={`\\underset{\\tiny \\text{непр.}}{\\LLL^1}[a,b]`}/>:
        <Math m="X"/> &mdash; множество непрерывных функций на <Math m="[a, b]"/>,<br/>
        и <Math m="d(f, g) = \int\limits_a^b \bigl|f(t) - g(t)\bigr| dt"/>.
    </ListItem>

    <ListItem>
        Пространство <Math m="\ell_\infty"/>, <br/>
        <Math m="X"/> &mdash; все ограниченные последовательности, и <Math m="d(a_n, b_n) = \sup |a_n - b_n|"/>.
    </ListItem>
    <ListItem>
        Подпространства <Math m="c"/> (сходящиеся последовательности) и <Math m="c_0"/> (бесконечно малые
        последовательности) метрического
        пространства <Math m="\ell_\infty"/> также являются метрическими.
    </ListItem>
    <ListItem>
        <Math m="p"/>-адическое метрическое пространство, <br/>
        <Math m="X = \ZZ"/>, и <Math m={`d(m, n) = p^{-a}`}/>, где <Math m="p^a"/> &mdash; наибольшая степень <Math
            m="p"/>, на
        которую делится <Math m="m-n"/>.
    </ListItem>
</BulletList>
</Par>

<Par>
<P>
    <b>Ультраметрическое пространство</b> <Math m="(X, d)"/> &mdash; особый вид метрического пространства, в котором
    метрика удовлетворяет усиленному неравенству треугольника
    <Math m={`d(x, y) <= \\max_{z \\in X} \\bigl\\{d(x, z), d(y, z)\\bigr\\}`}/>
</P>
</Par>

<Par>
<P>
</P>
</Par>
</section>
