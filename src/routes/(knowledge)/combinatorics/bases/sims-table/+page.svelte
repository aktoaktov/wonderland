<script>
    import Par from "$lib/Markup/Par.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import P from "$lib/Markup/P.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
</script>

<Title title="Таблицы Симса"
/>

<Par>
<P>
    Пусть у нас есть какая-то подгруппа <Math m={`G`}/> группы <Math m={`\\S_n`}/>.
    Эта перестановочная группа <Math m={`G`}/> действует
    на какое-то множество <Math m={`X`}/> из <Math m={`n`}/> элементов.
    Будем обозначать элементы этого множества числами, <Math m={`X = \\{1, 2, 3, \\dotsc, n-1, n\\}`}/>.
</P>
<P>
    Всё действие описывать сложно.
    А мы хотим компактно хранить действие и эффективно выполнять базовые тестовые операции.
    Чарльзом Симсом (Charles Sims) в 1960-х годах были предложены <b>таблицы Симса</b>
    для эффективного представления и анализа перестановочных групп (подгрупп <Math m={`\\S_n`}/>).
</P>
</Par>

<Par>
<P>
    Перейдем к более широкой и применимой постановке задачи.
</P>
<P>
    Мы по-прежнему рассматриваем перестановки элементов множества <Math m={`X = \\{1, 2, 3, \\dotsc, n-1, n\\}`}/>.
    Для простоты скажем, что группа перестановок элементов множества <Math m={`X`}/> совпадает с <Math m={`\\S_n`}/>.
    Точнее, <Math m={`\\Aut(X) \\isom \\S_n`}/>, а мы просто поставили тут знак равенства вместо изоморфности.
</P>
<P>
    Возьмём какое-то подмножество перестановок <Math m={`S \\subset \\S_n`}/>.
    Порождённая множеством <Math m={`S`}/> группа &mdash; группа <Math m={`\\langle S \\rangle`}/>,
    являющейся минимальной по включению подгруппой <Math m={`\\S_n`}/>, содержащей <Math m={`S`}/>.
    Мы типа дополнили множество <Math m={`S`}/> до группы.
</P>
<P>
    Мы хотим научиться для любого подмножества перестановок <Math m={`S \\subset \\S_n`}/>
</P>
<BulletList>
    <ListItem>
        Узнать порядок <Math m={`\\bigl| \\langle S \\rangle \\bigr|`}/>
    </ListItem>
    <ListItem>
        По перестановке <Math m={`\\sigma`}/> узнать, принадлежит ли она <Math m={`\\langle S \\rangle`}/>
    </ListItem>
    <ListItem>
        Создать итератор, выдающий все перестановки из <Math m={`\\langle S \\rangle`}/>
    </ListItem>
</BulletList>
</Par>

<Heading>Таблицы Симса и алгоритм Шрайера &ndash; Симса</Heading>

<Subheading>Хранение и представление</Subheading>

<Par>
<P>
    Пусть <Math m={`H`}/> &mdash; подгруппа некоторой конечной группы <Math m={`G`}/>.
</P>
<P>
    <b>Левая трансверсаль</b> <Math m={`G \\ltrans H`}/> &mdash; множество представителей
    левых смежных классов <Math m={`G`}/> по <Math m={`H`}/>, то есть
</P>
<Math display m={`G \\ltrans H \\defeq \\trans \\{ g \\cdot H \\mid \\forall g \\in G \\}`}/>
<P>
    Аналогично, <b>правая трансверсаль</b> <Math m={`G \\rtrans H`}/> &mdash; множество представителей
    правых смежных классов <Math m={`G`}/> по <Math m={`H`}/>, то есть
</P>
<Math display m={`G \\rtrans H \\defeq \\trans \\{ H \\cdot g \\mid \\forall g \\in G \\}`}/>
<P>
    Любой элемент <Math m={`g \\in G`}/> может быть единственным образом представлен как <Math m={`g = t \\cdot h`}/>,
    где <Math m={`t \\in G \\ltrans H`}/> и <Math m={`h \\in H`}/>.
    Или как <Math m={`g = h \\cdot t`}/>,
    где <Math m={`t \\in G \\rtrans H`}/> и <Math m={`h \\in H`}/>, и тоже единственным образом.
</P>
</Par>

<Theorem title="Лемма о представлении">
<P>
    Пусть
    <Math m={`G = G^{(0)} \\ge G^{(1)} \\ge G^{(2)} \\ge \\dotsb \\ge G^{(k-1)} \\ge G^{(k)} = \\{\\1\\}`}/>
    &mdash; ряд подгрупп группы <Math m={`G`}/>.
</P>
<P>
    Тогда любой элемент <Math m={`g \\in G`}/> может быть представлен в виде
</P>
<Math display
      m={`g = g_1 \\cdot g_2 \\dotsm g_k \\quad\\text{где}~
          g_j \\in G^{(j-1)} \\ltrans G^{(j)} ~\\text{для всех}~ 1 \\le j \\le k`}/>
<P>
    Или в виде
</P>
<Math display
      m={`g = g_k \\cdot g_{k-1} \\dotsm g_1 \\quad\\text{где}~
          g_j \\in G^{(j-1)} \\rtrans G^{(j)} ~\\text{для всех}~ 1 \\le j \\le k`}/>
</Theorem>

<Par>
<P>
    Сохраним все трансверсали (левые) в переменные <Math m={`S_1, S_2, \\dotsc, S_k`}/>,
    то есть <Math m={`S_j \\defeq G^{(j-1)} \\ltrans G^{(j)}`}/> для всех <Math m={`1 \\le j \\le k`}/>.
    Полученный набор трансверсалей называется <b>таблицей Симса</b> группы <Math m={`G`}/>.
</P>
<P>
    По лемме о представлении заключаем, что таблица Симса <Math m={`S_1, S_2, \\dotsc, S_k`}/>
    содержит всю информацию о группе <Math m={`G`}/>.
    То есть вместо хранения <Math m={`|G| = \\prod_{j=1}^k |S_j|`}/> объектов
    мы храним только <Math m={`\\sum_{j=1}^k |S_j|`}/>.
</P>
</Par>



<Par>
<P>
    <b>Узнать порядок <Math m={`|G|`}/>.</b>
    По теореме Лагранжа
</P>
<Math display m={`|G| = |S_1| \\cdot |S_2| \\dotsm |S_k|`}/>
<P>
    <b>Перечислить все перестановки из <Math m={`G`}/>.</b>
    Из леммы о представлении получаем, что нам достаточно просто перебрать все элементы из трансверсалей.
    Задача эквивалентна задаче генерации всех кортежей длины <Math m={`k`}/>,
    в которых на месте под номером <Math m={`j`}/> находится элемент из <Math m={`S_j`}/>.
</P>
<P>
    Можно представить каждую трансверсаль <Math m={`S_j`}/> как список, длина у всех таки списков своя.
    Получается, можно генерировать числа в смешанной системе счисления
    с основаниями <Math m={`|S_1|, |S_2|, \\dotsc, |S_k|`}/>,
    и рассматривать элементы кортежа как номера элементов в соответствующих трансверсалях.
</P>
</Par>

<Codeblock code={
`array[array] S[k]
iterator all_permutations:
    `
}/>

<Heading>Strong Generating Sets (SGS)</Heading>

<Heading>Schreier-Sims Algorithm</Heading>