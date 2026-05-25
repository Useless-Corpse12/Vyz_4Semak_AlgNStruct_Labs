
namespace SotoviyOperator.BackLayer.Sim_Cards
{
    public class SimC
    {
        public string Number    { get; set; } // Формат NNN-NNNNNNN
        public string Tariff    { get; set; }
        public int Year         { get; set; } //Год выпуска
        public bool IsAvailable   { get; set; }

        public SimC(string num, string trf, int yr, bool IsA) 
        { 
            Number = num;
            Tariff = trf;
            Year = yr;
            IsAvailable = IsA;
        }

    }
}
