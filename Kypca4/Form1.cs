using SotoviyOperator.BackLayer.Sim_Cards;
using SotoviyOperator.DataHandlers.Clients;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SotoviyOperator
{
    public partial class Main : Form
    {

        private Panel[] PanelMassive;
        private string[]  PanelNames;
        private ClientsHandler ClH = new ClientsHandler();
        private bool GridUPDTStop = false;
        public Main()
        {
            InitializeComponent();
            PanelMassive = new Panel[]  { Hello_panel, DEBUG_panel, Clients_panel, SimC_panel, Journal_panel };
            PanelNames   = new string[] { "", " : DEBUG", " : Клиенты", " : Sim - карты", " : Журнал" };
            this.Size = this.MinimumSize;
            this.Height += 180;
            for (int i = 0; i < PanelMassive.Length; i++) PanelMassive[i].Dock = DockStyle.Fill;    
            ClientPageRightPanel.Dock = DockStyle.Right;
            ClientGridView.Dock = DockStyle.Fill;
            SimCPageRightPanel.Dock = DockStyle.Right;
            SimCGridView.Dock = DockStyle.Fill;
            JournalPageRightPanel.Dock = DockStyle.Right;
            JournalGridView.Dock = DockStyle.Fill;
            Masterstroke.Items.Add(System.DateTime.Today.ToString("dd MMMM yyyy"));
            RefreshClientGrid();
            //PanelsResizeNRelocate();

        }

        private void hide_show_button_Click(object sender, EventArgs e)
        {
            Button hsbtn = (Button)sender;

            Navigation_panel.Visible = !Navigation_panel.Visible;

            hsbtn.Text = Navigation_panel.Visible ? "<" : ">";

            hsbtn.Location = Navigation_panel.Visible? new Point(Navigation_panel.Width - hsbtn.Width, 0) : new Point(0, 0);
        }
        private void PanelsReView(int numoopanele) 
        { 
            for (int i = 0; i < PanelMassive.Length; i++)
            {
                PanelMassive[i].Visible = i == numoopanele;
            }

            this.Text = "Обслуживание клиентов оператора сотовой связи" + PanelNames[numoopanele];

        }
        ///
        /// 0 - Приветствие
        /// 1 - Дебаг
        /// 2 - Клиенты
        /// 3 - Симки
        /// 4 - Журнал
        ///

        private void Hello_Click(object sender, EventArgs e)            => PanelsReView(0);

        private void Navigate_Clients_Click(object sender, EventArgs e) => PanelsReView(2);

        private void Navigate_SinC_Click(object sender, EventArgs e)    => PanelsReView(3);  

        private void Navigate_Journal_Click(object sender, EventArgs e) => PanelsReView(4); 

        private void DEBUG_Click(object sender, EventArgs e)            => PanelsReView(1); 

        private void Main_Resize(object sender, EventArgs e)
        {
           // PanelsResizeNRelocate();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.Text = $"{this.Width} : {this.Height}";
        }

        private void Clear_ClientButton_Click(object sender, EventArgs e)
        {
            ClientAdressTBox.Clear();
            ClientBDateTBox.Clear();
            ClientNameTBox.Clear();
            ClientPassATBox.Clear();
            ClientPasspTBox.Clear();
        }

        private void ReReding(object sender, EventArgs e){if (sender is TextBox tb && tb.BackColor == Color.LightCoral) { tb.Clear(); tb.BackColor = SystemColors.Window; }}

        private void Add_ClientButton_Click(object sender, EventArgs e)
        {
            bool isAlright = true;
            if (!Jabi_Algos.ClientPassportValidation(ClientPasspTBox.Text,out string confirmedPassp,out string pspmessage))
            {
                ClientPasspTBox.Text = pspmessage;
                isAlright = false;
                ClientPasspTBox.BackColor = Color.LightCoral;
            }

            if (!Jabi_Algos.ClientYearValidation(ClientBDateTBox.Text,out int Year, out string yearmessage))
            {
                ClientBDateTBox.Text = yearmessage;
                isAlright = false;
                ClientBDateTBox.BackColor = Color.LightCoral;
            }

            TextBox[] textBoxes = { ClientPassATBox, ClientNameTBox, ClientAdressTBox };

            foreach (TextBox TxBx in textBoxes)
            {
                if (string.IsNullOrEmpty(TxBx.Text))
                {
                    TxBx.BackColor = Color.LightCoral;
                    isAlright= false;
                    TxBx.Text = "Это поле должно быть заполнено";
                }
            }

            if (!isAlright) return;

            Client newCl = new Client(confirmedPassp,ClientPassATBox.Text,ClientNameTBox.Text,Year,ClientAdressTBox.Text);
            ClH.AddClient(newCl);
            RefreshClientGrid();
        }

        private void Clients_FilterOff_Click(object sender, EventArgs e)
        {
            RefreshClientGrid();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ((Button)sender).Text = HashTable.JHash1(((Button)sender).Text).ToString();
        }

        private void Del_ClientButton_Click(object sender, EventArgs e)
        {
            if (!(Jabi_Algos.DelClientPassportValidation(ClientPasspTBox.Text, out string confirmedPass, out string message)))
            {
                ClientPasspTBox.Text = message;
                ClientPasspTBox.BackColor = Color.LightCoral;
                return;
            }

            ClH.RmClient(confirmedPass);
            RefreshClientGrid();
        }

        private void RefreshClientGrid()
        {
            GridUPDTStop = true;
            ClientGridView.DataSource=ClH.GetIn();
            ClientGridView.ClearSelection();
            GridUPDTStop = false;
        }
        private void RefreshClientGrid(object source)
        {
            GridUPDTStop = true;
            ClientGridView.DataSource = source;
            ClientGridView.ClearSelection();
            GridUPDTStop = false;
        }

        private void ClientGridView_SelectionChanged(object sender, EventArgs e)
        {
            if (GridUPDTStop) return;
            if (ClientGridView.SelectedRows.Count > 0 && !ClientGridView.SelectedRows[0].IsNewRow)
            {
                TextBox[] textBoxes = {ClientPasspTBox, ClientPassATBox,ClientNameTBox,ClientBDateTBox, ClientAdressTBox };
                for ( int i = 0;i < textBoxes.Length; i++ )
                {
                    textBoxes[i].BackColor = SystemColors.Window;
                    textBoxes[i].Text = ClientGridView.SelectedRows[0].Cells[i].Value?.ToString();

                }
            }
        }

        private void NrASearch_ClientButton_Click(object sender, EventArgs e)
        {
            string ClSerchParam = ClientParametrSearchCBox.Text;
            if (string.IsNullOrEmpty(ClSerchParam)) return;
            if (ClSerchParam == "Год рождения" && !Jabi_Algos.ClientYearValidation(ClientParametrValueSearchTBox.Text, out int year,out string message))
            { ClientParametrValueSearchTBox.Text = message; ClientParametrValueSearchTBox.BackColor = Color.LightCoral; return; } 
            RefreshClientGrid(ClH.SearchByParameter(ClientParametrSearchCBox.Text, ClientParametrValueSearchTBox.Text));
        }


        private void ClientPassSearchBtn_Click(object sender, EventArgs e)
        {
            string indata = ClientPassSearchTBox.Text;
            if (!Jabi_Algos.ClientPassportValidation(indata, out string cnfpsp, out string message))
            {ClientPassSearchTBox.Text = message;ClientPassSearchTBox.BackColor= Color.LightCoral; return;}
            RefreshClientGrid(ClH.SearchByPassport(cnfpsp));
        }
    }
}
/*
                ClientPasspTBox.Text = ClientGridView.SelectedRows[0].Cells[0].Value?.ToString();
                ClientPassATBox.Text = ClientGridView.SelectedRows[0].Cells[1].Value?.ToString();
                ClientNameTBox.Text = ClientGridView.SelectedRows[0].Cells[2].Value?.ToString();
                ClientAdressTBox.Text = ClientGridView.SelectedRows[0].Cells[3].Value?.ToString();
                ClientBDateTBox.Text = ClientGridView.SelectedRows[0].Cells[4].Value?.ToString();
                */