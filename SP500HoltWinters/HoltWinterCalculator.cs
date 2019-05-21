using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SP500HoltWinters
{
    public class HoltWinterCalculator
    {
        private const decimal ALPHA = 0.8M;
        private const decimal BETA = 0.8M;
        private const decimal GAMA = 0.8M;

        private List<ItemLinha> _linhas;
        private int _tamanhoPeriodo;

        public HoltWinterCalculator(List<ItemLinha> linhas, int tamanhoPeriodo)
        {
            _linhas = linhas.OrderBy(l => l.Data).ToList();
            _tamanhoPeriodo = tamanhoPeriodo;
        }

        public List<ItemLinha> Calculate(int? timesForecasting)
        {
            Setup();
            return _linhas;
        }

        private void Setup()
        {
            for (int i = 0; i < _tamanhoPeriodo; i++)
            {
                var periodo = _linhas
                    .Skip(i)
                    .Take(_tamanhoPeriodo);

                _linhas[i].S = _linhas[i].Valor / periodo.Average(i => i.Valor);
            }
        }
    }
}
