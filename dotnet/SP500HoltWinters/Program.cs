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
            var fileName = "sp500input.csv";
            var skipHeader = true;
            var separator= ';';
            var outputFileName = "HoltWinters.csv";

            Console.WriteLine($"Carregando dados do arquivo [{fileName}] ...");

            var parser = new CsvParser<ItemLinha>(
                new CsvParserOptions(skipHeader, separator),
                new ItemLinhaMapper());

            Console.WriteLine($"Convertendo dados para objetos...");

            var linhas = parser
                .ReadFromFile(fileName, Encoding.UTF8)
                .Select(x => x.Result)
                .ToList();

            Console.WriteLine("Iniciando cálculo HoltWinters...");

            var calculator = new HoltWinterCalculator(linhas, 90);
            var result = calculator.Calculate(0);

            Console.WriteLine("Cálculos finalizados, iniciando criação do arquivo de saída...");

            using (var file = File.CreateText(outputFileName))
            {
                file.WriteLine($"Data;Valor;L;B;S;F;E;E%");

                foreach (var arr in result)
                {
                    file.WriteLine(string.Join(";", arr));
                }
            }

            Console.WriteLine($"Arquivo de saída criado com o nome [{outputFileName}]");
            Console.WriteLine("Processo finalizado.");
        }
    }
}
