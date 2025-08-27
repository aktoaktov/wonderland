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
</script>

<Title title="Числа Бернулли"
/>

<Par>
<P>
    Давайте для начала изучим сумму <Math m={`k`}/>-ых степеней чисел от <Math m={`1`}/> до <Math m={`n`}/>.
</P>
<Math display m={`S_k(n) \\defeq 1^k + 2^k + 3^k + \\dotsb + (n-1)^k + n^k = \\sum_{j=1}^n j^k`}/>
<P>
    Через бином Ньютона можно получить рекуррентную формулу
</P>
<Math display
      m={`S_k(n) = \\frac{1}{k+1} \\cdot \\Bigg( n^{k+1} + \\sum_{j=1}^k (-1)^{j+1} \\cdot \\binom{k+1}{j+1} \\cdot S_{k-j}(n) \\Bigg)`}/>

<P>
    Якоб Бернулли обнаружил закономерность в коэффициентах при <Math m={`n^j`}/>.
</P>
<Math display
      m={`S_k(n) = \\frac{1}{k+1} \\sum_{j=0}^k \\binom{k+1}{j} \\cdot B_j \\cdot n^{k+1-j}`}/>
<P>
    Коэффициенты <Math m={`B_j`}/> в этой формуле называются <b>числами Бернулли</b>.
</P>
</Par>


<Par>
<P>
    Из формулы можно получить неявное и явное рекуррентное соотношения для чисел Бернулли
</P>
<Math display
      m={`\\sum_{j=0}^k \\binom{k+1}{j} B_j = [k = 0] \\implies
          B_n = -\\frac{1}{n+1} \\sum_{k=1}^n \\binom{n+1}{k+1} `}/>
<P>
    Несколько первых значений чисел Бернулли
</P>
<Math display m={`B_0 = 1 \\quad B_1 = -\\frac{1}{2} \\quad B_2 = \\frac{1}{6} \\quad B_4 = -\\frac{1}{20} \\quad B_6 = \\frac{1}{42} \\quad B_8 = -\\frac{1}{30} \\quad B_{10} = \\frac{5}{66} \\quad B_{12} = -\\frac{691}{2730} \\quad\\dots\\quad B_{2k+1} = 0`}/>
</Par>