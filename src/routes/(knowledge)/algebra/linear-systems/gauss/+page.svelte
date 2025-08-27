<script>
  import Title from "$lib/Elements/Title.svelte"
  import Par from "$lib/Markup/Par.svelte"
  import P from "$lib/Markup/P.svelte"
  import Math from "$lib/Math/Math.svelte"
</script>

<Title title="Метод Гаусса"/>

<Par>
<P>
    Некоторые линейные преобразования обратимы, например, поворот на угол или растяжение.
    Другие необратимы, например проекция.
</P>
</Par>

<Par>
<P>
    Систему линейных уравнений
</P>
<Math display
      m={`\\cases{
          a_{1\\,1} \\cdot x_1 + a_{1\\,2} \\cdot x_2 + \\dotsb + a_{1\\,(n-1)} \\cdot x_{n-1} + a_{1\\,n} \\cdot x_n = b_1 \\\\
          a_{2\\,1} \\cdot x_1 + a_{2\\,2} \\cdot x_2 + \\dotsb + a_{2\\,(n-1)} \\cdot x_{n-1} + a_{2\\,n} \\cdot x_n = b_2 \\\\
          a_{3\\,1} \\cdot x_1 + a_{3\\,2} \\cdot x_2 + \\dotsb + a_{3\\,(n-1)} \\cdot x_{n-1} + a_{3\\,n} \\cdot x_n = b_3 \\\\
          \\cdots \\\\
          a_{n\\,1} \\cdot x_1 + a_{n\\,2} \\cdot x_2 + \\dotsb + a_{n\\,(n-1)} \\cdot x_{n-1} + a_{n\\,n} \\cdot x_n = b_n
          }`}/>
<P>
    можно записать как уравнение в матричной форме
</P>
<Math display m={`A \\cdot x = b`}/>
<P>
    Здесь
</P>
<Math display
      m={`A = \\pmatrix{
      a_{1\\,1} & a_{1\\,2} & \\cdots & a_{1\\,n} \\\\
      a_{2\\,1} & a_{2\\,2} & \\cdots & a_{2\\,n} \\\\
      \\vdots & \\vdots & \\ddots & \\vdots \\\\
      a_{n\\,1} & a_{n\\,2} & \\cdots & a_{n\\,n} \\\\
      } \\qquad
      b = \\pmatrix{b_1 \\\\ b_2 \\\\ \\vdots \\\\ b_n}
      \\qquad
      x = \\pmatrix{x_1 \\\\ x_2 \\\\ \\vdots \\\\ x_n}`}/>
<P>
    Для решения этого уравнения, то есть для нахождения вектора <Math m={`x`}/>, нужно обратить матрицу <Math m={`A`}/>
</P>
<Math display m={`x = A^{-1} \\cdot b`}/>
</Par>

<Par>
<P>
    Обратить матрицу <Math m={`A`}/> можно с помощью стандартной формулы
</P>
</Par>