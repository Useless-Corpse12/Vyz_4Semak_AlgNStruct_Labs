using System;
using System.Collections.Generic;
using System.Linq;

namespace SotoviyOperator.BackLayer.Sim_Cards
{
    
    public class SimCHandler
    {
        

        internal HashTable HT = new HashTable();

        public void AddSim(SimC inpSimC) => HT.Add(inpSimC);
        public void RmSim(SimC inpSimC) => HT.Remove(inpSimC.Number);
        public void RmSim(string inpNum) => HT.Remove(inpNum);

        public List<SimC> SearchSim(string parameter, string value)
        {

            List<SimC> result = new List<SimC>();
            if (parameter == "Номер") {result.Add(HT.Search(value)); return result; }

            List<SimC> allSimCs = HT.GetAll();
            switch (parameter)
            {

                case "Тариф":
                    result = allSimCs
                                    .Where(s => s.Tariff == value)
                                    .ToList();
                    break;

                case "Год":
                    result = allSimCs
                                    .Where(s => s.Year.ToString() == value)
                                    .ToList();
                    break;
                default: throw new ArgumentException($"Неизвестный параметр поиска: {parameter}");
            }
            return result;

        }


    }
}
