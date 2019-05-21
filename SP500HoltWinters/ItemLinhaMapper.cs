using System;
using TinyCsvParser.Mapping;
using TinyCsvParser.TypeConverter;

namespace SP500HoltWinters
{
    public class ItemLinhaMapper : CsvMapping<ItemLinha>
    {
        public ItemLinhaMapper()
        {
            MapProperty(0, i => i.Data);
            MapProperty(1, i => i.Valor, new ValorConverter());
        }
    }

    public class ValorConverter : ITypeConverter<decimal>
    {
        public Type TargetType => throw new NotImplementedException();

        public bool TryConvert(string value, out decimal result)
        {
            return decimal.TryParse(value.Replace(".", "").Replace(",", "."), out result);
        }
    }
}
