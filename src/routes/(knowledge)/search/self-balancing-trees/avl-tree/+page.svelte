<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Image from "$lib/Elements/Image.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"

    import imageRotate from './rotate.svg'
    import imageBigRotate from './big-rotate.svg'
</script>

<Title title="AVL дерево"
/>


<Heading>Фактор балансировки</Heading>

<Par>
    <P>
        Все проблемы несбалансированных деревьев из-за высоты. Точнее, из-за большой разности высот поддеревьев.
        Давайте на основе этой разности введем фактор балансировки.
    </P>
    <P>
        Для каждой вершины <Math m={`v`}/> определим <b>height balance factor</b> &mdash;
        разницу высот правого и левого поддеревьев.
    </P>
    <Math display m={`\\bf v = \\height(v.\\code{left}) - \\height(v.\\code{right})`}/>

    <P>
        Если balance factor у каких-то вершин по модулю большой, значит наше дерево перекашивает,
        и высота становится неприемлемой.
    </P>
</Par>

<Par>
    <P>
        Пусть <Math m={`|\\bf v| \\le b`}/> для всех вершин дерева.
        Давайте получим оценку высоты дерева.
    </P>
    <P>
        Пусть <Math m={`N(h)`}/> &mdash; минимальное количество вершин в дереве высоты <Math m={`h`}/>.
        Из определения следует, что <Math m={`N(0) = 0`}/> (пустое дерево) и <Math m={`N(1) = 1`}/> (только одна
        вершина).
    </P>
    <P>
        Для этого дерева выполнено условие баланса: <Math m={`|\\bf v| \\le b`}/> для всех вершин дерева.
        Тогда для дерева высоты <Math m={`h`}/> можно взять корень и разбить его на два поддерева.
        При этом для корня будет выполнено условие баланса. Значит,
    </P>
    <Math display m={`N(h) = 1 + N(h-1) + N(h-1-b)`}/>

    <P>
        Решение уравнения этого экспоненциальное.
        Давайте найдем точную оценку для <Math m={`N(h)`}/>, и, как следствие, для высоты <Math m={`h`}/>.
    </P>
</Par>

<Proof>
    <Par>
        <P>
            Запишем сразу производящую функцию для <Math m={`N(h)`}/>, учитывая, что <Math m={`h \\ge 0`}/>.
        </P>
        <Math display m={`G(x) = \\sum_{h=0}^\\oo N(h) \\cdot x^h`}/>

        <P>
            Подставим внутрь функции уравнение <Math m={`N(h) = 1 + N(h-1) + N(h-1-b)`}/>
        </P>
        <Math display
              m={`G(x) = \\sum_{h=0}^\\oo \\big(1 + N(h-1) + N(h-1-b) \\big) \\cdot x^h = \\frac{1}{1-x} + x \\cdot G(x) + x^{b+1} \\cdot G(x)`}/>

        <P>
            Мы получили производящую функцию
        </P>
        <Math display
              m={`G(x) = \\frac{1}{(1-x) \\cdot \\big( 1 - x - x^{b+1} \\big)}`}/>
        <P>
            Пусть полюсы функции <Math m={`G(x)`}/> &mdash; точка <Math m={`1`}/>
            и <Math m={`b+1`}/> точка <Math m={`\\rho_k`}/>,
            при этом точки <Math m={`\\rho_k`}/> являются решением уравнения <Math m={`1-x-x^{b+1} = 0`}/>.
            Тогда <Math m={`G(x)`}/> можно разложить в сумму простых дробей
        </P>
        <Math display
              m={`G(x) = - \\frac{1}{1-x} + \\sum_{k=0}^b \\frac{1}{(\\rho_k - 1) \\cdot (b \\rho_k - b - 1)} \\cdot \\frac{1}{1-x/\\rho_k}`}/>
    </Par>

    <Par>
        <P>
            Для удобства можно ввести другие переменные <Math m={`\\phi_k = 1/\\rho_k`}/>,
            которые являются корнями уравнения <Math m={`\\phi_k^{b+1} - \\phi_k^b - 1 = 0`}/>.
            Тогда формула для <Math m={`G(x)`}/> преобразуется в
        </P>
        <Math display
              m={`G(x) = - \\frac{1}{1-x} + \\sum_{k=0}^b \\frac{\\phi_k^2}{(\\phi_k - 1) \\cdot (b \\phi_k - b + \\phi_k)} \\cdot \\frac{1}{1 - \\phi_k \\cdot x}`}/>
    </Par>

    <Par>
        <P>
            Коэффициент <Math m={`N(h)`}/> при <Math m={`x^h`}/> в производящей функции <Math m={`G(x)`}/>
            вычисляются по теореме о представлении коэффициента рациональной производящей функции
        </P>
        <Math display
              m={`N(h) = -1 + \\sum_{k=0}^b \\frac{\\phi_k^{h+2}}{(\\phi_k - 1) \\cdot (b \\phi_k - b + \\phi_k)}`}/>

        <P>
            Можно вывести отсюда грубоватую асимптотическую оценку <Math m={`N(h)`}/>.
            Обозначим за <Math m={`\\phi`}/> единственный действительный положительный корень.
            У него же будет максимальный модуль, а значит он вносит наибольший вклад в асимптотику.
        </P>
        <Math display
              m={`N(h) = \\frac{\\phi^2}{(\\phi - 1) \\cdot (b \\phi - b + \\phi)} \\cdot \\phi^h - 1 + O \\big( \\phi^{-h} \\big)`}/>
    </Par>
</Proof>

<Par>
    <P>
        Теперь, зная <Math m={`N(h) = n`}/>, мы можем получить оценку высоты сбалансированного дерева
    </P>
    <Math display
          m={`h = \\frac{1}{\\log \\phi} \\cdot \\log n - \\frac{1}{\\log \\phi} \\cdot \\left( \\frac{\\phi^2}{(\\phi - 1) \\cdot (b \\phi - b + \\phi)} \\right) + \\frac{1}{n \\cdot \\log \\phi} + O \\left( \\frac{1}{n^2} \\right)`}/>
    <P>
        Какие выводы можно сделать?
        Если сильно нагрубить, можно сказать, что <Math m={`h = O \\big( \\log n \\big)`}/>,
        что было ясно еще при первом взгляде на рекурсивную формулу.
        А ещё, константы довольно маленькие, то есть мы можем позволить себе много свободы
        (в смысле взять довольно большое значение <Math m={`b`}/> без существенной просадки по высоте).
    </P>
</Par>


<Heading>Балансировка</Heading>

<Par>
    <P>
        Проще всего реализовать балансировку при требовании <Math m={`|\\bf v| \\le 1`}/> для всех вершин <Math
            m={`v`}/>.
    </P>
    <P>
        Итак, после операции вставки или удаления вершины дерево может перестать быть сбалансированным,
        то есть у какой-то вершины <Math m={`|\\bf v| > 1`}/>. Надо научиться возвращать дереву баланс.
    </P>
    <P>
        Важное наблюдение заключается в том, что после вставки или удалении вершины balance factor
        может измениться только тех у вершин, которые лежат на пути от корня до вставленной или удаленной вершины.
        И изменяется он на <Math m={`1`}/> или на <Math m={`-1`}/>.
        Это позволяет вынести балансировку дерева в две процедуры,
        которые будут вызываться после каждой вставки и после каждого удаления.
    </P>
</Par>


<Subheading>Поворот</Subheading>

<Par>
    <P>
        Обычный поворот относительно вершины выравнивает высоты её
        поддеревьев. После поворота высота дерева не увеличивается, то есть
        уменьшается на <Math m={`1`}/> или остается неизменной.
    </P>
</Par>

<Image src={imageRotate}/>

<Par>
    <P>
        Если <Math m={`\\bf A = 2`}/>, то осуществляем правый поворот. Если
        <Math m={`\\bf A = -2`}/>, то левый поворот.
    </P>
</Par>

<Codeblock code={
`function rotate_right(node a):
    node b = a.left
    a.left = b.right
    b.right = a
    height adjustment a
    height adjustment b`
}/>

<Codeblock code={
`function rotate_left(node a):
    node b = a.right
    a.right = b.left
    b.left = a
    height adjustment a
    height adjustment b`
}/>

<Subheading>Большой поворот</Subheading>

<Par>
    <P>
        В результате обычного поворота balance factor у вершины B может стать
        <Math m={`2`}/> или <Math m={`-2`}/>, и дерево снова будет
        разбалансированным. Эту проблему решают большие повороты влево и
        вправо, которые состоят из двух обычных поворотов: у вершины и у ее
        ребёнка.
    </P>
</Par>

<Image src={imageBigRotate}/>

<Codeblock code={
`function big_rotate_left(node a):
    rotate_right(a.right)
    rotate_left(a)`
}/>

<Codeblock code={
`function big_rotate_right(node a):
    rotate_left(a.left)
    rotate_right(a)`
}/>


<Heading>Слабые AVL деревья</Heading>