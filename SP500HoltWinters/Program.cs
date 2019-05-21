using System;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading;
using TinyCsvParser;

namespace SP500HoltWinters
{
    class Program
    {
        static void Main(string[] args)
        {
            Thread.CurrentThread.CurrentCulture = new CultureInfo("pt-BR");

            var parser = new CsvParser<ItemLinha>(
                new CsvParserOptions(true, ';'),
                new ItemLinhaMapper());

            var linhas = parser
                .ReadFromFile("input.csv", Encoding.UTF8)
                .Select(x => x.Result)
                .ToList();

            var calculator = new HoltWinterCalculator(linhas, 90);
            var result = calculator.Calculate(0);

            using (var file = File.CreateText("HoltWinters.csv"))
            {
                file.WriteLine($"Data;Valor;L;B;S;F;E;E%");

                foreach (var arr in result)
                {
                    file.WriteLine(string.Join(";", arr));
                }
            }

            Console.ReadKey();
        }
    }
}
