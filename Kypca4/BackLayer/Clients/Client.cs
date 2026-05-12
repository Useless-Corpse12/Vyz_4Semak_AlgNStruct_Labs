using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SotoviyOperator
{
    public class Client
    {
        public string Passport      { get; set; } //NNNN-NNNNNN
        public string PassportData  { get; set; } //Дата и место выдачи. Зачем?
        public string FullName      { get; set; } //ФИО
        public int    Year          { get; set; } //Год Рождения
        public string Adress        { get; set; } //Адрес

        public Client(string passport,string passportdata,string fullname, int year, string adress) 
        { 
            Passport = passport;
            PassportData = passportdata;
            FullName = fullname;
            Year = year;
            Adress = adress;
        }

    }
}
