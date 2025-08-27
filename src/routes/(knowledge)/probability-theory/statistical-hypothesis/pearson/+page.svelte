<script>
import Title from "$lib/Elements/Title.svelte"
import Par from "$lib/Markup/Par.svelte"
import P from "$lib/Markup/P.svelte"
import Math from "$lib/Math/Math.svelte"
</script>

<Title title="Критерий Пирсона"
/>

<Par>
    <P>
        Пусть каждый исход может принадлежать одной из <Math m="k"/> категорий.
        Теоретическая вероятность того, что исход будет принадлежать категории <Math m="i"/> равна <Math m="p_i"/>.
    </P>
    <P>
        Мы проводим <Math m="n"/> <b>независимых</b> испытаний и для каждой категории <Math m="i"/> считаем
        количество получившихся исходов <Math m="y_i"/>, которые ей реально принадлежат.
    </P>
    <P>
        Образуем статистику <Math m="\chi^2"/>
    </P>
    <Math display m={`\\chi^2 \\defeq \\sum_{i=1}^k \\frac{(y_i - n \\cdot p_i)^2}{n \\cdot p_i}`}/>
    <P>
        Учитывая, что <Math m="y_1 + y_2 + \dotsb + y_k = n"/> и <Math m="p_1 + p_2 + \dotsb + p_k = 1"/>,
        можем упростить вычисление статистики <Math m="\chi^2"/>
    </P>
    <Math display m={`\\chi^2 = ...`}/>
</Par>