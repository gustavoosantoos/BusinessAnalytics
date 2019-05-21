using System;

namespace SP500HoltWinters
{
    public class ItemLinha
    {
        public DateTime Data { get; set; }
        public decimal Valor { get; set; }
        public decimal L { get; set; }
        public decimal B { get; set; }
        public decimal S { get; set; }
        public decimal F { get; set; }
        public decimal E { get; set; }
        public decimal EPerc { get; set; }

        public override string ToString()
        {
            return $"{Data.ToShortDateString()};{Valor};{L};{B};{S};{F};{E};{EPerc}";
        }
    }
}
