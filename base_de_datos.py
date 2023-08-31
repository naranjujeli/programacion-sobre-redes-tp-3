# https://www.espn.co.uk/football/story/_/id/37633460/2022-world-cup-all-squad-lists-qatar

# Info de ejemplo
### Borrar y cargar con sus datos
_info = {'grupos': {
            'grupo A': [{'nombre': 'Quatar', 'arqueros': ['Saad Al-Sheeb', 'Meshaal Barsham', 'Yousef Hassan'], 
                                             'defensores': ['Pedro Miguel', 'Musaab Khidir', 'Tarek Salman', 'Bassam Al-Rawi', 'Boualem Khoukhi', 'Abdelkarim Hassan', 'Homam Ahmed', 'Jassem Gaber'],
                                             'mediocampistas': ['Ali Asad', 'Assim Madabo', 'Mohammed Waad', 'Salem Al-Hajri', 'Moustafa Tarek', 'Karim Boudiaf', 'Abdelaziz Hatim', 'Ismail Mohamad'],
                                             'delanteros': ['Naif Al-Hadhrami', 'Ahmed Alaaeldin', 'Hassan Al-Haydos', 'Khalid Muneer', 'Akram Afif', 'Almoez Ali', 'Mohamed Muntari']},
                        {'nombre': 'Ecuador', 'arqueros': ['Moises Ramirez', 'Alexander Dominguez', 'Hernan Galindez'],
                                              'defensores': ['Piero Hincapie', 'Robert Arboleda', 'Pervis Estupinan', 'Angelo Preciado', 'Jackson Porozo', 'Xavier Arreaga', 'Felix Torres', 'Diego Palacios', 'William Pacho'],
                                              'mediocampistas': ['Carlos Gruezo', 'Jose Cifuentes', 'Alan Franco', 'Moises Caicedo', 'Angel Mena', 'Jeremy Sarmiento', 'Ayrton Preciado', 'Sebastian Mendez', 'Gonzalo Plata', 'Romario Ibarra'],
                                              'delanteros': ['Djorkaeff Reasco', 'Kevin Rodriguez', 'Michael Estrada', 'Enner Valencia']},
                        {'nombre': 'Paises Bajos', 'arqueros': ['Justin Bijlow', 'Andries Noppert', 'Remko Pasveer'],
                                              'defensores': ['Virgil van Dijk', 'Nathan Ake', 'Daley Blind', 'Jurrien Timber', 'Denzel Dumfries', 'Stefan de Vrij', 'Matthijs de Ligt', 'Tyrell Malacia', 'Jeremie Frimpong'],
                                              'mediocampistas': ['Frenkie de Jong', 'Steven Berghuis', 'Davy Klaassen', 'Teun Koopmeiners', 'Marten de Roon', 'Cody Gakpo', 'Kenneth Taylor', 'Xavi Simons'],
                                              'delanteros': ['Memphis Depay', 'Steven Bergwijn', 'Vincent Janssen', 'Luuk de Jong', 'Noa Lang', 'Wout Weghorst']},
                        {'nombre': 'Senegal', 'arqueros': ['Edouard Mendy', 'Alfred Gomis', 'Seny Dieng'], 
                                              'defensores': ['Kalidou Koulibaly', 'Abdou Diallo', 'Youssouf Sabaly', 'Fode Ballo-Toure', 'Pape Abdou Cisse', 'Ismail Jakobs', 'Formose Mendy', 'Moussa NDiaye'],
                                              'mediocampistas': ['Idrissa Gueye', 'Cheikhou Kouyate', 'Nampalys Mendy', 'Krepin Diatta', 'Pape Gueye', 'Pape Matar Sarr', 'Pathe Ciss', 'Moustapha Name', 'Loum Ndiaye'],
                                              'delanteros': ['Ismaila Sarr', 'Boulaye Dia', 'Bamba Dieng', 'Famara Diedhiou', 'Nicolas Jackson', 'Iliman Ndiaye']}],

            'grupo B': [{'nombre': 'Inglaterra', 'arqueros': ['Jordan Pickford', 'Aaron Ramsdale', 'Nick Pope'], 
                                                 'defensores': ['Kieran Trippier', 'Trent Alexander-Arnold', 'Kyle Walker', 'Ben White', 'Harry Maguire', 'John Stones', 'Eric Dier', 'Conor Coady', 'Luke Shaw'],
                                                 'mediocampistas': ['Declan Rice', 'Jude Bellingham', 'Kalvin Phillips', 'Jordan Henderson', 'Conor Gallagher', 'Mason Mount'],
                                                 'delanteros': ['Harry Kane', 'Callum Wilson', 'Marcus Rashford', 'Raheem Sterling', 'Bukayo Saka', 'Phil Foden', 'Jack Grealish', 'James Maddison']},
                        {'nombre': 'Iran', 'arqueros': ['Alireza Beiranvand', 'Amir Abedzadeh', 'Hossein Hosseini', 'Payam Niazmand'],
                                           'defensores': ['Ehsan Hajsafi', 'Morteza Pouraliganji', 'Ramin Rezaeian', 'Milad Mohammadi', 'Hossein Kanani', 'Shojae Khalilzadeh', 'Sadegh Moharrami', 'Rouzbeh Cheshmi', 'Majid Hosseini', 'Abolfazl Jalali'],
                                           'mediocampistas': ['Ahmad Noorollahi', 'Saman Ghoddos', 'Vahid Amiri', 'Saeid Ezatolahi', 'Alireza Jahanbakhsh', 'Mehdi Torabi', 'Ali Gholizadeh', 'Ali Karimi'],
                                           'delanteros': ['Karim Ansarifard', 'Sardar Azmoun', 'Mehdi Taremi']},
                        {'nombre': 'USA', 'arqueros': ['Matt Turner', 'Sean Johnson', 'Ethan Horvath'],
                                          'defensores': ['Cameron Carter-Vickers', 'Sergino Dest', 'Aaron Long', 'Shaq Moore', 'Tim Ream', 'Antonee Robinson', 'Joe Scally', 'DeAndre Yedlin', 'Walker Zimmerman'],
                                          'mediocampistas': ['Brenden Aaronson', 'Kellyn Acosta', 'Tyler Adams', 'Luca de la Torre', 'Weston McKennie', 'Yunus Musah', 'Cristian Roldan'],
                                          'delanteros': ['Jesus Ferreira', 'Jordan Morris', 'Christian Pulisic', 'Gio Reyna', 'Joshua Sargent', 'Timothy Weah', 'Haji Wright']},
                        {'nombre': 'Wales', 'arqueros': ['Wayne Hennessey', 'Danny Ward', 'Adam Davies'],
                                              'defensores': ['Ben Davies', 'Ben Cabango', 'Tom Lockyer', 'Joe Rodon', 'Chris Mepham', 'Ethan Ampadu', 'Chris Gunter', 'Neco Williams', 'Connor Roberts'],
                                              'mediocampistas': ['Sorba Thomas', 'Joe Allen', 'Matthew Smith', 'Dylan Levitt', 'Harry Wilson', 'Joe Morrell', 'Jonny Williams', 'Aaron Ramsey', 'Rubin Colwill'],
                                              'delanteros': ['Gareth Bale', 'Kieffer Moore', 'Mark Harris', 'Brennan Johnson', 'Daniel James']}],
                        
            'grupo C': [{'nombre': 'Argentina', 'arqueros': ['Emiliano Martinez', 'Geronimo Rulli', 'Franco Armani'],
                                  'defensores': ['Nahuel Molina', 'Gonzalo Montiel', 'Cristian Romero', 'German Pezzella', 'Nicolas Otamendi', 'Lisandro Martinez', 'Marcos Acuna', 'Nicolas Tagliafico', 'Juan Foyth'],
                                  'mediocampistas': ['Rodrigo De Paul', 'Leandro Paredes', 'Alexis Mac Allister', 'Guido Rodriguez', 'Papu Gomez', 'Enzo Fernandez', 'Exequiel Palacios'],
                                  'delanteros': ['Lionel Messi', 'Angel Di Maria', 'Lautaro Martinez', 'Julian Alvarez', 'Paulo Dybala', 'Angel Correa', 'Thiago Almada']},
                        {'nombre': 'Arabia Saudita', 'arqueros': ['Mohamed Al-Owais', 'Nawaf Al-Aqidi', 'Mohamed Al-Yami'],
                                              'defensores': ['Yasser Al-Shahrani', 'Ali Al-Bulaihi', 'Abdulelah Al-Amri', 'Abdullah Madu', 'Hassan Tambakti', 'Sultan Al-Ghanam', 'Mohammed Al-Breik', 'Saud Abdulhamid'],
                                              'mediocampistas': ['Salman Al-Faraj', 'Riyadh Sharahili', 'Ali Al-Hassan', 'Mohamed Kanno', 'Abdulelah Al-Malki', 'Sami Al-Najei', 'Abdullah Otayf', 'Nasser Al-Dawsari ', 'Abdulrahman Al-Aboud', 'Salem Al-Dawsari', 'Hattan Bahebri'],
                                              'delanteros': ['Haitham Asiri', 'Saleh Al-Shehri', 'Firas Al-Buraikan']},
                        {'nombre': 'Mexico', 'arqueros': ['Guillermo Ochoa', 'Alfredo Talavera', 'Rodolfo Cota'],
                                              'defensores': ['Kevin Alvarez', 'Nestor Araujo', 'Gerardo Arteaga', 'Jesus Gallardo', 'Hector Moreno', 'Cesar Montes', 'Jorge Sanchez', 'Johan Vasquez'],
                                              'mediocampistas': ['Edson Alvarez', 'Roberto Alvarado', 'Uriel Antuna', 'Luis Chavez', 'Andres Guardado', 'Erick Gutierrez', 'Hector Herrera', 'Orbelin Pineda', 'Carlos Rodriguez', 'Luis Romo'],
                                              'delanteros': ['Rogelio Funes Mori', 'Raul Jimenez', 'Hirving Lozano ', 'Henry Martin', 'Alexis Vega']},
                        {'nombre': 'Polonia', 'arqueros': ['Wojciech Szczesny', 'Bartlomiej Dragowski', 'Lukasz Skorupski'],
                                              'defensores': ['Jan Bednarek', 'Kamil Glik', 'Robert Gumny', 'Artur Jedrzejczyk', 'Jakub Kiwior', 'Mateusz Wieteska', 'Bartosz Bereszynski', 'Matthew Cash', 'Nicola Zalewski'],
                                              'mediocampistas': ['Krystian Bielik', 'Przemyslaw Frankowski ', 'Kamil Grosicki', 'Grzegorz Krychowiak', 'Jakub Kaminski', 'Michal Skoras', 'Damian Szymanski', 'Sebastian Szymanski', 'Piotr Zielinski', 'Szymon Zurkowski'],
                                              'delanteros': ['obert Lewandowski', 'Arkadiusz Milik', 'Krzysztof Piatek', 'Karol Swiderski']}],

            'grupo D': [{'nombre': 'Francia', 'arqueros': ['Alphonse Areola', 'Hugo Lloris', 'Steve Mandanda'],
                                  'defensores': ['Axel Disasi', 'Lucas Hernandez', 'Theo Hernandez', 'Ibrahima Konate', 'Jules Kounde', 'Benjamin Pavard', 'William Saliba', 'Dayot Upamecano', 'Raphael Varane'],
                                  'mediocampistas': ['Eduardo Camavinga', 'Youssouf Fofana', 'Matteo Guendouzi', 'Adrien Rabiot', 'Aurelien Tchouameni', 'Jordan Veretout'],
                                  'delanteros': ['Kingsley Coman', 'Ousmane Dembele', 'Olivier Giroud', 'Antoine Griezmann', 'Kylian Mbappe', 'Marcus Thuram', 'Randal Kolo Muani']},
                        {'nombre': 'Australia', 'arqueros': ['Mat Ryan', 'Andrew Redmayne', 'Danny Vukovic'],
                                              'defensores': ['Milos Degenek', 'Aziz Behich', 'Joel King', 'Nathaniel Atkinson', 'Fran Karacic', 'Harry Souttar', 'Kye Rowles', 'Bailey Wright', 'Thomas Deng'],
                                              'mediocampistas': ['Aaron Mooy', 'Jackson Irvine', 'Ajdin Hrustic', 'Keanu Baccus', 'Cameron Devlin', 'Riley McGree'],
                                              'delanteros': ['Awer Mabil', 'Mathew Leckie', 'Jamie Maclaren', 'Jason Cummings', 'Mitchell Duke', 'Garang Kuol', 'Craig Goodwin', 'Marco Tilio']},
                        {'nombre': 'Dinamarca', 'arqueros': ['Kasper Schmeichel', 'Oliver Christensen', 'Frederik Ronnow'],
                                              'defensores': ['Alexander Bah', 'Simon Kjaer', 'Joachim Andersen', 'Joakim Maehle', 'Andreas Christensen', 'Rasmus Kristensen', 'Jens Stryger Larsen', 'Victor Nelsson', 'Daniel Wass'],
                                              'mediocampistas': ['Thomas Delaney', 'Mathias Jensen', 'Christian Eriksen', 'Pierre-Emile Hojbjerg', 'Christian Norgaard', 'Robert Skov'],
                                              'delanteros': ['Andreas Cornelius', 'Martin Braithwaite', 'Kasper Dolberg', 'Mikkel Damsgaard', 'Jesper Lindstrom', 'Yussuf Poulsen', 'Andreas Skov Olsen', 'Jonas Wind']},
                        {'nombre': 'Tunes', 'arqueros': ['Aymen Dahmen', 'Bechir Ben Said', 'Mouez Hassen', 'Aymen Mathlouthi'],
                                              'defensores': ['Ali Abdi', 'Dylan Bronn', 'Mohamed Drager', 'Nader Ghandri', 'Bilel Ifa', 'Wajdi Kechrida', 'Ali Maaloul', 'Yassine Meriah', 'Montassar Talbi'],
                                              'mediocampistas': ['Mohamed Ali Ben Romdhane', 'Ghaylane Chaalali', 'Aissa Laidouni', 'Hannibal Mejbri', 'Ferjani Sassi', 'Elyas Skhiri'],
                                              'delanteros': ['Anis Ben Slimane', 'Seifeddine Jaziri', 'Issam Jebali', 'Wahbi Khazri', 'Taha Yassine Khenissi', 'Youssef Msakni', 'Naim Sliti']}],

            'grupo E': [{'nombre': 'Espana', 'arqueros': ['Unai Simon', 'Robert Sanchez', 'David Raya'],
                                  'defensores': ['Dani Carvajal', 'Cesar Azpilicueta', 'Eric Garcia', 'Hugo Guillamon', 'Pau Torres', 'Aymeric Laporte', 'Jordi Alba', 'Alex Balde'],
                                  'mediocampistas': ['Sergio Busquets', 'Rodri', 'Gavi', 'Carlos Soler', 'Marcos Llorente', 'Pedri', 'Koke'],
                                  'delanteros': ['Ferran Torres', 'Nico Williams', 'Yeremi Pino', 'Alvaro Morata', 'Marco Asensio', 'Pablo Sarabia', 'Dani Olmo', 'Ansu Fati']},
                        {'nombre': 'Alemania', 'arqueros': ['Manuel Neuer', 'Marc-Andre ter Stegen', 'Kevin Trapp'],
                                              'defensores': ['Matthias Ginter', 'Antonio Rudiger', 'Niklas Sule', 'Nico Schlotterbeck', 'Thilo Kehrer', 'David Raum', 'Lukas Klostermann', 'Armel Bella-Kotchap', 'Christian Gunter'],
                                              'mediocampistas': ['Ilkay Gundogan', 'Jonas Hofmann', 'Leon Goretzka', 'Serge Gnabry', 'Leroy Sane', 'Jamal Musiala', 'Joshua Kimmich', 'Thomas Muller', 'Julian Brandt', 'Mario Gotze'],
                                              'delanteros': ['Kai Havertz', 'Youssoufa Moukoko', 'Niclas Fullkrug', 'Karim Adeyemi']},
                        {'nombre': 'Costa Rica', 'arqueros': ['Keylor Navas', 'Esteban Alvarado', 'Patrick Sequeira'],
                                                 'defensores': ['Francisco Calvo', 'Juan Pablo Vargas', 'Kendall Waston', 'Oscar Duarte', 'Daniel Chacon', 'Keysher Fuller', 'Carlos Martinez', 'Bryan Oviedo', 'Ronald Matarrita'],
                                                 'mediocampistas': ['Yeltsin Tejeda', 'Celso Borges', 'Youstin Salas', 'Roan Wilson', 'Gerson Torres', 'Douglas Lopez', 'Jewison Bennette', 'Alvaro Zamora', 'Anthony Hernandez', 'Brandon Aguilera', 'Bryan Ruiz'],
                                                 'delanteros': ['Joel Campbell', 'Anthony Contreras', 'Johan Venegas']},
                        {'nombre': 'Japon', 'arqueros': ['Shuichi Gonda', 'Daniel Schmidt', 'Eiji Kawashima'],
                                              'defensores': ['Miki Yamane', 'Hiroki Sakai', 'Maya Yoshida', 'Takehiro Tomiyasu', 'Shogo Taniguchi', 'Ko Itakura', 'Hiroki Ito', 'Yuto Nagatomo'],
                                              'mediocampistas': ['Wataru Endo', 'Hidemasa Morita', 'Ao Tanaka', 'Gaku Shibasaki', 'Kaoru Mitoma', 'Daichi Kamada', 'Ritsu Doan', 'Junya Ito', 'Takumi Minamino', 'Takefusa Kubo', 'Yuki Soma'],
                                              'delanteros': ['Daizen Maeda', 'Takuma Asano', 'Shuto Machino', 'Ayase Ueda']}],

            'grupo F': [{'nombre': 'Belgica', 'arqueros': ['Thibaut Courtois', 'Simon Mignolet', 'Koen Casteels'],
                                  'defensores': ['Jan Vertonghen', 'Toby Alderweireld', 'Leander Dendoncker', 'Zeno Debast', 'Arthur Theate', 'Wout Faes'],
                                  'mediocampistas': ['Hans Vanaken', 'Axel Witsel', 'Youri Tielemans', 'Amadou Onana', 'Kevin De Bruyne', 'Yannick Carrasco', 'Thorgan Hazard', 'Timothy Castagne', 'Thomas Meunier'],
                                  'delanteros': ['Romelu Lukaku', 'Michy Batshuayi', 'Lois Openda', 'Charles De Ketelaere', 'Eden Hazard', 'Jeremy Doku', 'Dries Mertens', 'Leandro Trossard']},
                        {'nombre': 'Canada', 'arqueros': ['James Pantemis', 'Milan Borjan', 'Dayne St. Clair'],
                                              'defensores': ['Samuel Adekugbe', 'Joel Waterman', 'Alistair Johnston', 'Richie Laryea', 'Kamal Miller', 'Steven Vitoria', 'Derek Cornelius'],
                                              'mediocampistas': ['Liam Fraser', 'Ismael Kone', 'Mark-Anthony Kaye', 'David Wotherspoon', 'Jonathan Osorio', 'Atiba Hutchinson', 'Stephen Eustaquio', 'Samuel Piette'],
                                              'delanteros': ['Tajon Buchanan', 'Liam Millar', 'Lucas Cavallini', 'Ike Ugbo', 'Junior Hoilett', 'Jonathan David', 'Cyle Larin', 'Alphonso Davies']},
                        {'nombre': 'Croacia', 'arqueros': ['Dominik Livakovic', 'Ivica Ivusic', 'Ivo Grbic'],
                                              'defensores': ['Domagoj Vida', 'Dejan Lovren', 'Borna Barisic', 'Josip Juranovic', 'Josko Gvardiol', 'Borna Sosa', 'Josip Stanisic', 'Martin Erlic', 'Josip Sutalo'],
                                              'mediocampistas': ['Luka Modric', 'Mateo Kovacic', 'Marcelo Brozovic', 'Mario Pasalic', 'Nikola Vlasic', 'Lovro Majer', 'Kristijan Jakic', 'Luka Sucic'],
                                              'delanteros': ['Ivan Perisic', 'Andrej Kramaric', 'Bruno Petkovic', 'Mislav Orsic', 'Ante Budimir', 'Marko Livaja']},
                        {'nombre': 'Marruecos', 'arqueros': ['Bono', 'Munir El Kajoui', 'Ahmed Tagnaouti'],
                                              'defensores': ['Nayef Aguerd', 'Yahia Attiyat Allah', 'Badr Benoun', 'Achraf Dari', 'Jawad El Yamiq', 'Achraf Hakimi', 'Noussair Mazraoui', 'Romain Saiss'],
                                              'mediocampistas': ['Sofyan Amrabat', 'Selim Amallah', 'Bilal El Khannous', 'Yahya Jabrane', 'Azzedine Ounahi', 'Abdelhamid Sabiri'],
                                              'delanteros': ['Zakaria Aboukhlal', 'Sofiane Boufal', 'Ilias Chair', 'Walid Cheddira', 'Youssef En-Nesyri', 'Abde Ezzalzouli', 'Abderrazak Hamdallah', 'Amine Harit', 'Hakim Ziyech']}],

            'grupo G': [{'nombre': 'Brasil', 'arqueros': ['Alisson', 'Ederson', 'Weverton'],
                                  'defensores': ['Dani Alves', 'Danilo', 'Alex Sandro', 'Alex Telles', 'Bremer', 'Eder Militao', 'Marquinhos', 'Thiago Silva'],
                                  'mediocampistas': ['Bruno Guimaraes', 'Casemiro', 'Everton Ribeiro', 'Fabinho', 'Fred', 'Lucas Paqueta'],
                                  'delanteros': ['Antony', 'Gabriel Jesus', 'Gabriel Martinelli', 'Neymar', 'Pedro', 'Raphinha', 'Richarlison', 'Rodrygo', 'Vinicius Junior']},
                        {'nombre': 'Camerun', 'arqueros': ['Andre Onana', 'Devis Epassy', 'Simon Ngapandouetnbu'],
                                              'defensores': ['Jean-Charles Castelletto', 'Enzo Ebosse', 'Collins Fai', 'Olivier Mbaizo', 'Nouhou Tolo', 'Nicolas Nkoulou', 'Christopher Wooh'],
                                              'mediocampistas': ['Olivier Ntcham', 'Gael Ondoua', 'Martin Hongla', 'Pierre Kunde', 'Samuel Oum Gouet', 'Andre-Frank Zambo Anguissa', 'Jerome Ngom'],
                                              'delanteros': ['Nicolas Ngamaleu', 'Christian Bassogog', 'Bryan Mbeumo', 'Georges-Kevin Nkoudou', 'Jean-Pierre Nsame', 'Vincent Aboubakar', 'Karl Toko-Ekambi', 'Eric Maxim Choupo-Moting', 'Souaibou Marou']},
                        {'nombre': 'Serbia', 'arqueros': ['Marko Dmitrovic', 'Predrag Rajkovic', 'Vanja Milinkovic-Savic'],
                                              'defensores': ['Stefan Mitrovic', 'Nikola Milenkovic', 'Strahinja Pavlovic', 'Milos Veljkovic', 'Filip Mladenovic', 'Strahinja Erakovic', 'Srdjan Babic'],
                                              'mediocampistas': ['Nemanja Gudelj', 'Sergej Milinkovic-Savic', 'Sasa Lukic', 'Marko Grujic', 'Filip Kostic', 'Uros Racic', 'Nemanja Maksimovic', 'Ivan Ilic', 'Andrija Zivkovic', 'Darko Lazovic'],
                                              'delanteros': ['Dusan Tadic', 'Aleksandar Mitrovic', 'Dusan Vlahovic', 'Filip Djuricic', 'Luka Jovic', 'Nemanja Radonjic']},
                        {'nombre': 'Suiza', 'arqueros': ['Gregor Kobel', 'Yann Sommer', 'Jonas Omlin', 'Philipp Kohn'],
                                              'defensores': ['Manuel Akanji', 'Eray Comert', 'Nico Elvedi', 'Fabian Schar', 'Silvan Widmer', 'Ricardo Rodriguez', 'Edimilson Fernandes'],
                                              'mediocampistas': ['Michel Aebischer', 'Xherdan Shaqiri', 'Renato Steffen', 'Granit Xhaka', 'Denis Zakaria', 'Fabian Frei', 'Remo Freuler', 'Noah Okafor', 'Fabian Rieder', 'Ardon Jashari'],
                                              'delanteros': ['Breel Embolo', 'Ruben Vargas', 'Djibril Sow', 'Haris Seferovic', 'Christian Fassnacht']}],

            'grupo H': [{'nombre': 'Portugal', 'arqueros': ['Diogo Costa', 'Jose Sa', 'Rui Patricio'],
                                  'defensores': ['Diogo Dalot', 'Joao Cancelo', 'Danilo Pereira', 'Pepe', 'Ruben Dias', 'Antonio Silva', 'Nuno Mendes', 'Raphael Guerreiro'],
                                  'mediocampistas': ['Joao Palhinha', 'Ruben Neves', 'Bernardo Silva', 'Bruno Fernandes', 'Joao Mario', 'Matheus Nunes', 'Vitinha', 'William Carvalho', 'Otavio'],
                                  'delanteros': ['Cristiano Ronaldo', 'Joao Felix', 'Rafael Leao', 'Ricardo Horta', 'Goncalo Ramos', 'Andre Silva']},
                        {'nombre': 'Uruguay', 'arqueros': ['Fernando Muslera', 'Sergio Rochet', 'Sebastian Sosa'],
                                              'defensores': ['Ronald Araujo', 'Sebastian Coates', 'Martin Caceres', 'Guillermo Varela', 'Matias Vina', 'Mathias Olivera', 'Jose Maria Gimenez', 'Diego Godin', 'Jose Luis Rodríguez'],
                                              'mediocampistas': ['Lucas Torreira', 'Matias Vecino', 'Rodrigo Bentancur', 'Manuel Ugarte', 'Giorgian de Arrascaeta', 'Nicolas de la Cruz', 'Federico Valverde ', 'Facundo Pellistri', 'Agustin Canobbio', 'Facundo Torres'],
                                              'delanteros': ['Luis Suarez', 'Darwin Nunez', 'Maximiliano Gomez', 'Edinson Cavani']},
                        {'nombre': 'Korea Del Sur', 'arqueros': ['Kim Seung-Gyu', 'Jo Hyeon-Woo', 'Song Bum-Keun'],
                                              'defensores': ['Kim Min-Jae', 'Kim Young-Gwon', 'Kwon Kyung-Won', 'Cho Yu-Min', 'Kim Moon-Hwan', 'Yoon Jong-Gyu', 'Kim Tae-Hwan', 'Kim Jin-Su', 'Hong Chul'],
                                              'mediocampistas': ['Jung Woo-Young', 'Son Jun-Ho', 'Paik Seung-Ho', 'Hwang In-Beom', 'Lee Jae-Sung', 'Kwon Chang-Hoon', 'Jeong Woo-Yeong', 'Lee Kang-In', 'Son Heung-Min', 'Hwang Hee-Chan', 'Na Sang-Ho', 'Song Min-Kyu'],
                                              'delanteros': ['Hwang Ui-Jo', 'Cho Gue-Sung']},
                        {'nombre': 'Ghana', 'arqueros': ['Arquero 1', 'Arquero 2', 'Arquero 3'],
                                              'defensores': [],
                                              'mediocampistas': [],
                                              'delanteros': []}]},
        'Campion': 'Argentina'}

#Obtener jugadores: que dado un equipo te da todos sus jugadores.
def obtener_jugadores(equipo):
    res = []
    for pos in {'arqueros', 'defensores', 'mediocampistas', 'delanteros'}:
        res += equipo[pos]

    return res

#Obtener arqueros: que te da todos los arqueros de todos los equipos.
def obtener_arqueros():
    res = []
    for grupo in _info['Grupos']:
        for equipo in grupo:
            res += equipo['arqueros']
    return res

#Obtener equipos: que te da los nombres de los 32 equipos.
def obtener_equipos():
    res = []
    for grupo in _info['Grupos']:
        for equipo in grupo:
            res += equipo['nombre']
    return res

#Obtener ganador: que te da el nombre del campeón del mundo.
def obtener_ganador():
    return _info['Campion']