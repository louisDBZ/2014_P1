// unity.h

using namespace std;

#include <string> 
#include <iostream> 
enum typeofunit { fantassin_lourd, fantassin_leger,char_leger,char_lourd,canon_lourd,canon_leger, camion, halftrack, unite_de_motos, reconnaissance_vehiculee} ;
enum typeofprotection { mur , sans_protection , maison,arbre  };
const int taille_tab_portee_degat=10;
const int taille_tab_deplacement=3;

void affichertypeunit(typeofunit type){
    switch(type){
        case fantassin_leger :
            cout<<"fantassin_leger";
            break;
        case fantassin_lourd:
            cout <<"fantassin_lourd";break;
        case char_leger :
            cout<<"char_leger";
            break;
        case char_lourd:
            cout <<"char_lourd";break;
        case canon_lourd:
            cout <<"canon_lourd";break;
        case canon_leger:
            cout <<"canon_leger";break;
    }

}
//fantassin_lourd , fantassin_leger, char_leger, char_lourd, canon_leger, canon_lourd, éclaireur, transport_camion
class unity { 
public : 

 unity (typeofunit type2, string name2);


 void setnbsoldat(int nbsoldat2){  nbsoldat=nbsoldat2;}; 
 void setdetetectee(bool detectee2){  nbsoldat=detectee2;};
void setdeplacement(int i, int terrain ){ deplacement[terrain]=i;}


typeofunit gettype(){return type;}
int fight_unity_one_each_other( unity unit2, int distance_adv, typeofprotection proctection_adv , typeofprotection proctection2);
void attacked_by_unit2( unity unit2, int distance_adv , typeofprotection proctection2);

void afficher(){ 
    affichertypeunit(type);
    
    cout<< " "<<name <<": nbsoldat="<< nbsoldat<< endl;  };
bool verifcombatpossible(unity  unit2);
void afficher_tableau_degat(){
     cout << "portee degat"<<endl;
    for(int k=0; k<taille_tab_portee_degat; k++) {
            if (tableau_portee_degat[k]!=NULL )
            cout << k <<"       "<<tableau_portee_degat[k]<<endl;
            else return;
    }
}

void afficher_tableau_deplacement(){
     cout << "rush  route terrain_accidenté"<<endl;
    for(int k=0; k<taille_tab_deplacement; k++) {
            if (deplacement[k]!=NULL )
            cout <<" "<< deplacement[k]<<"     ";
            else return;
    }
    cout<< endl;
}

void afficher_datasheet(){

    cout<<endl<< " detectee "<< detectee<<endl; 
      cout<< endl;
afficher_tableau_deplacement();
cout<< endl;
afficher_tableau_degat();
cout<< endl;
}

private: 

string name;
int nbsoldatdebase;
int nbsoldat;
int deplacement[taille_tab_deplacement]; 
int visibilitee;
bool detectee;
typeofunit type;
int nbdetourrechargement;
int current_tourrechargement;
int tableau_portee_degat[taille_tab_portee_degat];
string renseignement; 

};


