using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace SotoviyOperator.DataHandlers.Clients
{
    public class ClientsHandler
    {
        private readonly AVLTree _tree = new AVLTree();
        public List<Client> SearchByParameter(string parameter, string value)
        {
            var allClients = _tree.PreOrder();
            var result = new List<Client>();

            switch (parameter)
            {

                case "ФИО":
                    foreach (var client in allClients)
                        if (Jabi_Algos.StraightSearch(client.FullName, value))
                            result.Add(client);
                    break;

                case "Адрес":
                    foreach (var client in allClients)
                        if (Jabi_Algos.StraightSearch(client.Adress, value))
                            result.Add(client);
                    break;

                case "Год рождения":
                    if (int.TryParse(value, out int year))
                        foreach (var client in allClients)
                            if (client.Year == year)
                                result.Add(client);
                    break;

                default:
                    throw new ArgumentException($"Неизвестный параметр поиска: {parameter}");
            }

            return result;
        }

        public List<Client> SearchByPassport(string passport)
        {
            List <Client> result = new List<Client>();
            result.Add(_tree.Search(passport));
            return result;
        }

        public void RmClient(string passport)
        {
            _tree.Delete(passport);
        }

        public void AddClient(Client client)
        {
            _tree.Insert(client);
        }

        public List<Client> GetPre()
        {
            return _tree.PreOrder();
        }

        public List<Client> GetIn()
        {
            return _tree.InOrder();
        }
    }
}
