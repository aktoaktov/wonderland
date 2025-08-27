<script>
    import Title from "$lib/Elements/Title.svelte"
    import Statement from "$lib/Stencils/Blocks/Statement.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
</script>

<Title title="Градиентный спуск"
/>

<Statement title="Задача оптимизации">
    <P>
        Пусть <Math m={`f \\colon \\RR^n \\to \\RR`}/>.
        Мы хотим решить задачу оптимизации
    </P>
    <Math display m={`\\min_{x \\in \\RR^n} f(x)`}/>
</Statement>

<Par>
    <P>
        Будем искать решение задачи итеративно.
        Пусть <Math m={`x_k \\in \\RR`}/> &mdash; какое-то приближённое решение задачи,
        полученное нами на <Math m={`k`}/>-ом шаге.
    </P>

    <P>
        Давайте будем двигаться в направлении наискорейшего спуска, которое задается антиградиентом <Math
            m={`-\\nabla f`}/>.
    </P>

    <Math display m={`x_{k+1} = x_k - \\alpha \\cdot \\nabla f (x_k)`}/>
</Par>

<Par>
    <P>
        Как выбрать величину <Math m={`\\alpha`}/> нашего шага?
    </P>
</Par>

<Subheading>Скорость сходимости</Subheading>

<Par>
    <P>
        Для оценки скорости сходимости алгоритмов градиентного спуска придется использовать некоторые допущения.
    </P>
    <P>
        Итак, для функции <Math m={`f \\colon \\RR^n \\to \\RR`}/>
        мы хотим найти <Math m={`x^* = \\argmin_{x \\in \\RR^n} f(x)`}/>.
    </P>
    <P>
        Действуем мы итеративным методом, который на <Math m={`k`}/>-м шаге выдает нам решение <Math m={`x_k`}/>.
        При этом начинаем алгоритм мы с точки <Math m={`x_0`}/>, которая находится от оптимума на расстоянии не более
        <Math m={`R`}/>.
    </P>
    <Math display m={`\\|x_0 - x^*\\| \\le R`}/>

    <P>
        Все действия будут происходить в <Math m={`R`}/>-окрестности точки <Math m={`x^*`}/>.
    </P>
    <P>
        Функция <Math m={`f`}/> <Math m={`\\mu`}/>-сильно выпукла
    </P>
    <Math display m={`f(y) \\ge f(x) + \\nabla f (x) ^\\T \\cdot (y - x) + \\frac{\\mu}{2} \\cdot \\|y-x\\|^2`}/>

    <P>
        и её градиент <Math m={`\\nabla f`}/> <Math m={`L`}/>-липшицев.
    </P>
    <Math display m={`\\| \\nabla f (x) - \\nabla f (y) \\| \\le L \\cdot \\|x-y\\|`}/>
</Par>

<Par>
    <P>
        Мы хотим научиться оценивать скорость сходимости. Для этого целесообразно ввести расстояние до оптимума <Math
            m={`d_k`}/> на <Math m={`k`}/>-м шаге:
    </P>
    <Math display m={`d_k = \\|x_k - x^*\\|`}/>
    <P>
        Давайте сразу получим все важные соотношения, которые нам будут нужны для получения оценок.
    </P>
</Par>
<Par>
    <P>
        Поскольку <Math m={`x^*`}/> &mdash; точка минимума, градиент <Math m={`\\nabla f (x^*) = \\0`}/>.
        Из липшицевости градиента можно получить ограничение на градиент в любой точке <Math m={`x_k`}/>:
    </P>
    <Math display
          m={`\\| \\nabla f (x_k) \\| = \\| \\nabla f (x_k) - \\nabla f (x^*) \\| \\le L \\cdot \\| x_k - x^* \\| = L \\cdot d_k`}/>
</Par>
<Par>
    <P>
        Используем свойство сильной выпуклости функции
    </P>
    <Math display
          m={`f(x^*) \\ge f(x_k) + \\nabla f (x_k) ^\\T \\cdot (x^* - x_k) + \\frac{\\mu}{2} \\cdot \\|x^*-x_k\\|^2`}/>

    <P>
        <Math m={`x^*`}/> &mdash; точка минимума <Math m={`f`}/>,
        а значит <Math m={`f(x^*) - f(x_k) \\le 0`}/> для любой точки <Math m={`x_k`}/>.
        Подставляем в предыдущую формулу
    </P>
    <Math display
          m={`0 \\ge \\nabla f (x_k) ^\\T \\cdot (x^* - x_k) + \\frac{\\mu}{2} \\cdot \\|x^*-x_k\\|^2`}/>

    <P>
        Из этого неравенства получаем, что
    </P>
    <Math display m={`\\nabla f (x_k) ^\\T \\cdot (x_k - x^*) \\ge \\frac{\\mu}{2} \\cdot \\|x_k - x^*\\|^2`}/>
</Par>

<Heading>Постоянная скорость</Heading>
<Par>
    <P>
        Чем больше градиент, тем &laquo;круче&raquo; функция.
        Давайте, руководствуясь этими соображениями, сделаем скорость спуска постоянной.
    </P>
    <P>
        Выберем константу <Math m={`\\eta`}/>, называемую в машинном обучении learning rate.
        Формула расчета следующего положения будет такая
    </P>
    <Math display m={`x_{k+1} = x_k - \\eta \\cdot \\nabla f (x_k)`}/>
</Par>

<Theorem title="Скорость сходимости градиентного спуска с постоянной скоростью">
    <P>
        Пусть <Math m={`f \\colon \\RR^n \\to \\RR`}/> &mdash; выпуклая функция.
        Мы хотим найти <Math m={`x^* = \\argmin_{x \\in \\RR^n} f(x)`}/>.
    </P>

    <P>
        Для этого мы используем алгоритм градиентного спуска с постоянной скоростью <Math m={`\\eta`}/>
    </P>
    <Math display m={`x_{k+1} = x_k - \\eta \\cdot \\nabla f (x_k)`}/>

    <P>
        Если функция <Math m={`f`}/> <Math m={`\\mu`}/>-сильно выпуклая
        и её градиент <Math m={`\\nabla f`}/> <Math m={`L`}/>-липшицева, то
    </P>
    <Math display m={`d_{k+1} \\le \\sqrt{1 + \\eta^2 L^2 - \\eta \\mu} \\cdot d_k`}/>

    <P>
        и в самом плохом случае алгоритм сходится при <Math m={`\\eta \\lt \\frac{\\mu}{L^2}`}/>,
        а наибыстрейшая сходимость обеспечивается при <Math m={`\\eta = \\frac{\\mu}{2L^2}`}/>.
    </P>
</Theorem>

<Proof>
    <P>
        Возьмем формулу шага, вычтем из левой и правой частей <Math m={`x^*`}/> и посчитаем квадрат нормы
    </P>
    <Math display m={`d_{k+1}^2 = \\|x_{k+1} - x^*\\|^2 = \\big\\| (x_k - x^*) - \\eta \\cdot \\nabla f (x_k) \\big\\|^2`}/>

    <P>
        Воспользуемся тождеством <Math m={`\\|a-b\\|^2 = \\|a\\|^2 - 2 \\cdot a ^\\T \\cdot b + \\|b\\|^2`}/>
    </P>
    <Math display m={`d_{k+1}^2 = \\|x_k - x^*\\|^2 - 2 \\eta \\cdot \\nabla f (x_k) ^\\T \\cdot (x_k - x^*) + \\eta^2 \\cdot \\| \\nabla f (x_k) \\|^2`}/>

    <P>
        Применим выведенные в разделе ... оценки и получим формулу
    </P>
    <Math display m={`d_{k+1}^2 \\le d_k^2 - 2 \\eta \\cdot \\frac{\\mu}{2} \\cdot d_k^2 + \\eta^2 L^2 \\cdot d_k^2`}/>
    <Math display m={`d_{k+1} \\le \\sqrt{1 - \\eta \\mu + \\eta^2 L^2} \\cdot d_k`}/>

    <P>
        Максимальная скорость гарантируется минимальным множителем перед <Math m={`d_k`}/> в этой рекуррентной формуле.
        Для того, чтобы множитель был минимальным, learning rate должен быть равен <Math m={`\\frac{\\mu}{2L^2}`}/>.
    </P>
</Proof>


<Heading>Фиксированный шаг</Heading>
<Par>
    <P>
        Можно сделать так, чтобы мы шагали на фиксированную длину <Math m={`l`}/>.
        Тогда формула расчета следующего положения будет такая
    </P>

    <Math display m={`x_{k+1} = x_k - l \\cdot \\frac {\\nabla f (x_k)}{\\|\\nabla f (x_k)\\|}`}/>

    <P>
        Шаг постоянный, поэтому этот вариант алгоритма устойчив к резким изменениям градиента.
        Если функция пологая (градиент очень маленький), мы будем довольно долго подбираться к оптимуму.
    </P>

    <P>
        Главный минус фиксированного шага &mdash; маленькая точность. Давайте найдем предельную точность алгоритма.
    </P>
</Par>

<Theorem title="Предельная точность градиентного спуска с фиксированным шагом">
    <P>
        Пусть <Math m={`f \\colon \\RR^n \\to \\RR`}/> &mdash; выпуклая функция.
        Мы хотим найти <Math m={`x^* = \\argmin_{x \\in \\RR^n} f(x)`}/>.
    </P>

    <P>
        Для этого мы используем алгоритм градиентного спуска с фиксированным шагом <Math m={`l`}/>
    </P>
    <Math display m={`x_{k+1} = x_k - l \\cdot \\frac {\\nabla f (x_k)}{\\|\\nabla f (x_k)\\|}`}/>

    <P>
        При этом <Math m={`f`}/> &mdash; сильно выпуклая функция с параметром <Math m={`\\mu`}/>:
    </P>
    <Math display m={`f(y) \\ge f(x) + \\nabla f (x) ^\\T \\cdot (y - x) + \\frac{\\mu}{2} \\cdot \\|y-x\\|^2`}/>

    <P>
        и градиент <Math m={`\\nabla f`}/> липшицев с константой <Math m={`L`}/>:
    </P>
    <Math display m={`\\| \\nabla f (x) - \\nabla f (y) \\| \\le L \\cdot \\|x-y\\|`}/>
</Theorem>

<Proof>
    <P>
        Оценим расстояние до минимума.
        Пусть <Math m={`d_k = \\|x_k - x^*\\|`}/> &mdash; расстояние до минимума на шаге <Math m={`k`}/>.
    </P>
    <P>
        Алгоритм делает шаг согласно формуле
    </P>
    <Math display m={`x_{k+1} = x_k - l \\cdot \\frac {\\nabla f (x_k)}{\\|\\nabla f (x_k)\\|}`}/>

    <P>
        Вычитаем <Math m={`x^*`}/> и считаем квадрат нормы
    </P>
    <Math display
          m={`\\| x_{k+1} - x^* \\|^2 = \\left\\| (x_k - x^*) - l \\cdot \\frac {\\nabla f (x_k)}{\\|\\nabla f (x_k)\\|} \\right\\|^2`}/>

    <P>
        Раскрыв квадрат нормы и переписываем в терминах расстояний до минимума. Получим формулу
    </P>
    <Math display
          m={`d_{k+1}^2 = d_k^2 - 2 \\cdot l \\cdot \\frac {\\nabla f (x_k) ^\\T \\cdot (x_k - x^*)}{\\|\\nabla f (x_k)\\|} + l^2`}/>

    <P>
        Нам нужно как-то оценить страшный коэффициент с градиентом.
    </P>

    <P>
        Используем свойство сильной выпуклости функции
    </P>
    <Math display
          m={`f(x^*) \\ge f(x_k) + \\nabla f (x_k) ^\\T \\cdot (x^* - x_k) + \\frac{\\mu}{2} \\cdot \\|x^*-x_k\\|^2`}/>

    <P>
        <Math m={`x^*`}/> &mdash; точка минимума <Math m={`f`}/>,
        а значит <Math m={`f(x^*) - f(x_k) \\le 0`}/> для любой точки <Math m={`x_k`}/>.
        Подставляем в предыдущую формулу
    </P>
    <Math display
          m={`0 \\ge \\nabla f (x_k) ^\\T \\cdot (x^* - x_k) + \\frac{\\mu}{2} \\cdot \\|x^*-x_k\\|^2`}/>

    <P>
        Из этого неравенства получаем, что
    </P>
    <Math display m={`\\nabla f (x_k) ^\\T \\cdot (x_k - x^*) \\ge \\frac{\\mu}{2} \\cdot \\|x_k - x^*\\|^2`}/>

    <P>
        Используем липшицевость градиента, учитывая, что <Math m={`\\nabla f (x^*) = \\0`}/>
    </P>
    <Math display
          m={`\\| \\nabla f (x_k) \\| = \\| \\nabla f(x_k) - \\nabla f (x^*) \\| \\le L \\cdot \\| x_k - x^* \\| = L \\cdot d_k`}/>

    <P>
        Применим эти два неравенства для оценки страшного коэффициента
    </P>
    <Math display
          m={`\\frac {\\nabla f (x_k) ^\\T \\cdot (x_k - x^*)}{\\|\\nabla f (x_k)\\|} \\ge \\frac{\\frac{\\mu}{2} \\cdot d_k^2}{L \\cdot d_k} = \\frac{\\mu}{2L} \\cdot d_k`}/>

    <P>
        В итоге получаем формулу для рекуррентного вычисления расстояния до оптимума
    </P>
    <Math display m={`d_{k+1}^2 \\le d_k^2 - \\frac{\\mu l}{L} \\cdot d_k + l^2`}/>
</Proof>