//unity.cpp


#include <iostream>
using namespace std; 
#include "unity.h"
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <stdio.h>      /* printf, scanf, puts, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h> 
#include <random>
#include <iostream>
#include <random>

unity::unity (typeofunit type2, string name2){
type=type2;
name=name2;

if (type2 == fantassin_lourd){
    nbsoldatdebase=5;
    nbsoldat=5;
    deplacement[0] = 3;
deplacement[2] = 1;
deplacement[1] = 2;
     visibilitee = 3 ;
 detectee=0 ;
}
else if (type2 == fantassin_leger){
    nbsoldatdebase=6;
    nbsoldat=6;
    renseignement ="ne peut attaquer un char";
       deplacement[0] = 3;
deplacement[2] = 1;
deplacement[1] = 2;
    visibilitee = 5 ;
    detectee=0 ;
    tableau_portee_degat[0]=20;
    tableau_portee_degat[1]=10;
    tableau_portee_degat[2]=8;
    tableau_portee_degat[3]=6;}

 else if (type2 == char_leger){
    nbsoldatdebase=8; //point de vie pour un char
    nbsoldat=8;
       deplacement[0] = 3;
deplacement[2] = 1;
deplacement[1] = 2;
    visibilitee = 3 ;
    detectee=0 ;
    tableau_portee_degat[0]=10;
    tableau_portee_degat[1]=9;
    tableau_portee_degat[2]=8;
    tableau_portee_degat[3]=7;
    tableau_portee_degat[4]=6;
    tableau_portee_degat[5]=0;
}

else if (type2 == char_lourd){
    nbsoldatdebase=12;
    nbsoldat=12;
       deplacement[0] = 2;
deplacement[2] = 1;
deplacement[1] = 0;
    visibilitee = 2 ;
    detectee=0 ;
    tableau_portee_degat[0]=12;
    tableau_portee_degat[1]=10;
    tableau_portee_degat[2]=9;
    tableau_portee_degat[3]=8;
    tableau_portee_degat[4]=7;
    tableau_portee_degat[5]=5;
 }

 else if (type2 == canon_leger){
    nbsoldatdebase=3; //point de vie pour un char
    nbsoldat=8;
       deplacement[0] = 2;
deplacement[2] = 1;
deplacement[1] = 2;
    visibilitee = 4 ;
    detectee=0 ;
    tableau_portee_degat[0]=10;
    tableau_portee_degat[1]=9;
    tableau_portee_degat[2]=8;
    tableau_portee_degat[3]=7;
    tableau_portee_degat[4]=6;
    tableau_portee_degat[5]=0;
}

else if (type2 == canon_lourd){
    nbsoldatdebase=4;
    nbsoldat=4;
       deplacement[0] = 1;
deplacement[2] = 0;
deplacement[1] = 0;
    visibilitee = 4 ;
    detectee=0 ;
    tableau_portee_degat[0]=12;
    tableau_portee_degat[1]=10;
    tableau_portee_degat[2]=9;
    tableau_portee_degat[3]=8;
    tableau_portee_degat[4]=7;
    tableau_portee_degat[5]=5;
 }
}
int frand_a_b2(int a, int b){
    return ( rand()/(int)RAND_MAX ) * (b-a) + a;
}

int* init_sans_doublons(int a, int b){
	int taille = b-a;
	int* resultat;
    resultat= new int[taille] ;//*sizeof (int));
	int i=0;
	// On remplit le tableau de manière à ce qu'il soit trié
	for(i = 0; i< taille; i++){
		resultat[i]=i+a;
	}
	return resultat;
}

void melanger(int* tableau, int taille){
	int i=0;
	int nombre_tire=0;
	int temp=0;
	
	for(i = 0; i< taille;i++){
		nombre_tire=frand_a_b2(0,taille);
		// On échange les contenus des cases i et nombre_tire
		temp = tableau[i];
		tableau[i] = tableau[nombre_tire];
		tableau[nombre_tire]=temp;
	}
}



void alea (){

    CallableType myVariable{};              // créé une variable de type CallableType
auto result = myVariable(arg1, arg2);

    std::random_device rd{};            // création du générateur
 
    std::cout << rd()<< rd()<<rd()<< rd()<< rd() << rd() << std::endl;     // génération d'un nombre aléatoire
    std::cout << rd() < rd()<<rd()<< rd()<< rd() << rd()<< std::endl;     // génération d'un nombre aléatoire
    std::cout << rd() < rd()<<rd()<< rd()<< rd() << rd()<< std::endl;
}



/*

int randomnumber(int de){

    int i = 0;
	int nombre_aleatoire = 0;
	srand(time(NULL)); // initialisation de rand
	for(i=0; i<5; i++){
		nombre_aleatoire = rand();
		//printf("%d ",nombre_aleatoire);
	}
    return nombre_aleatoire;

}
*/
double frand_a_b(double a, double b){

//cout << "debut"<<endl;
        // A ne pas oublier !
        srand(time(NULL));
        
        int i0 =0;
        int* t=NULL; // Va contenir le tableau de nombres
       
        // On commence pour de vrai ici :
        t=init_sans_doublons(a,b);
        melanger(t,b-a);
        
        printf("La suite aléatoire est : ");
        for(i0=0; i0<b-a; i0++){
                //printf("%d ",t[i0]);
        }
        printf("\n");
        
        // Ne pas oublier de libérer le tableau
        free(t);

        cout<<"t="<< t[frand_a_b2(a,b)];

cout<<endl;



    int i = 0;
	int nombre_aleatoire = 0;
	//srand(time(NULL)); // initialisation de rand
	for(i=0; i<5; i++){
        nombre_aleatoire =( (rand()/(double)RAND_MAX ) * (b-a) )+ a; // rand renvoie un entier entre rand et rand max
    
	}
    return nombre_aleatoire;
}

bool unity::verifcombatpossible(unity  unit2){

if( ((unit2.type ==fantassin_leger)&&((type==char_leger)||(type==char_lourd))  ))
    return false;
    cout<<"pb: le combat ne peut avoir lieu"<<endl;

return true;
}

 int unity::fight_unity_one_each_other(  unity unit2, int distance_adv, typeofprotection proctection_adv , typeofprotection proctection2){

verifcombatpossible( unit2);

     cout << endl<< "fight "<<endl;

int calcul_degat_ennemi =0;
int calcul_degat =0;

//test frand
int n;
//for(int k=0;k<20;k++){
;//}

int m;
//for(int k=0;k<20;k++){
//}

//randomnumber(12);

//cout << "nombre_aleatoire=" << n <<endl;

int protection=0;
int nb_mort=0;
int nb_mort_adv=0;

if(proctection_adv==sans_protection){protection =0;}
else if(proctection_adv==mur){protection =5;}
else if(proctection_adv==maison){protection =10;}

for (int i=0 ;i<nbsoldat;i++){
    cout <<endl;
    n=frand_a_b(1,13);
    cout << "nombre_aleatoire attaque=" << n <<endl;
    m=frand_a_b(1,6);
    cout << "nombre_aleatoire def=" << m <<endl;
    cout<< "dégat infligé par le soldat" <<i<<" = ";
    calcul_degat=  tableau_portee_degat[distance_adv] * n -m * protection ;
    cout<< calcul_degat<<endl;



if ( calcul_degat > 100 && unit2.gettype()==fantassin_leger ){

    nb_mort_adv++;
}
else if ( calcul_degat > 40 && ((type==canon_leger)||(type==canon_lourd)) ){
    nb_mort++;
}
else if ( calcul_degat > 90 && ((type==char_leger)||(type==char_lourd)) ){
    nb_mort++;nb_mort++;nb_mort++;
}


}



//_one_each_other


if(proctection2==sans_protection){protection =0;}
else if(proctection2==mur){protection =5;}
else if(proctection2==maison){protection =10;}

for (int i=0 ;i<unit2.nbsoldat;i++){
    cout <<endl;
    n=frand_a_b(1,13);
    cout << "nombre_aleatoire attaque=" << n <<endl;
    m=frand_a_b(1,6);
    cout << "nombre_aleatoire def=" << m <<endl;
    cout<< "dégat infligé par le soldat" <<i<<" = ";
    calcul_degat=  tableau_portee_degat[distance_adv] * n -m * protection ;
    cout<< calcul_degat<<endl;



if ( calcul_degat > 100 && type==fantassin_leger ){

    nb_mort++;
}
}
// affichage du nombre d'unité tuées

cout <<endl<< "BILAN"<<endl<<"l'unite ";//<<unit2.type
affichertypeunit(unit2.type);

cout<<" "<<unit2.name<<" a perdu "<<nb_mort_adv<<" hommes. RIP"<<endl;
// affichage du nombre d'unité tuées

cout << "l'unite ";//<<unit2.type
affichertypeunit(type);

cout<<" "<<name<<" a perdu "<<nb_mort<<" hommes. RIP"<<endl<<endl;


//mise mise a jour 

// changement du nombre de soldat de mon unité 
if (nbsoldat-nb_mort>0){
nbsoldat= nbsoldat - nb_mort;}
else {nbsoldat = 0;}


//  renvoie nombre de soldat de l'unité adverse

if (unit2.nbsoldat-nb_mort_adv>0){
    cout<<"in "<< unit2.nbsoldat- nb_mort_adv<<endl;
    return unit2.nbsoldat- nb_mort_adv;}
else {return 0;}


//unit2.unity::setdetetectee(1);
/*

int nbsoldat_origin = unit1.nbsoldat;
int nbsoldat_origin2 = unit2.nbsoldat;

unit1.attacked_by_unit2( unity unit2, int distance_adv,  typeofprotection proctection2)
unit2.attacked_by_unit2(  unit2, int distance_adv,  typeofprotection proctection2)*/
 }


 void unity::attacked_by_unit2( unity unit2, int distance_adv,  typeofprotection proctection2){

     cout << endl<< "fight "<<endl;

//int calcul_degat_ennemi =0;
int calcul_degat =0;

//test frand
int n;
//for(int k=0;k<20;k++){
;//}

int m;
//for(int k=0;k<20;k++){
//}

//randomnumber(12);

//cout << "nombre_aleatoire=" << n <<endl;

int protection=0;
int nb_mort=0;
//int nb_mort_adv=0;

//_one_each_other


if(proctection2==sans_protection){protection =0;}
else if(proctection2==mur){protection =5;}
else if(proctection2==maison){protection =10;}

for (int i=0 ;i<unit2.nbsoldat;i++){
    cout <<endl;
    n=frand_a_b(1,13);
    cout << "nombre_aleatoire attaque=" << n <<endl;
    m=frand_a_b(1,6);
    cout << "nombre_aleatoire def=" << m <<endl;
    cout<< "dégat infligé par le soldat" <<i<<" = ";
    calcul_degat=  tableau_portee_degat[distance_adv] * n -m * protection ;
    cout<< calcul_degat<<endl;



if ( calcul_degat > 100 && ((type==fantassin_leger)||(type==fantassin_lourd)) ){
    nb_mort++;
}
else if ( calcul_degat > 40 && ((type==canon_leger)||(type==canon_lourd)) ){
    nb_mort++;
}
else if ( calcul_degat > 90 && ((type==char_leger)||(type==char_lourd)) ){
    nb_mort++;nb_mort++;nb_mort++;
}
}
// affichage du nombre d'unité tuées

cout <<endl<< "BILAN"<<endl<<"l'unite ";//<<unit2.type
affichertypeunit(type);

cout<<" "<<name<<" a perdu "<<nb_mort<<" hommes. RIP"<<endl;


//mise mise a jour 

// changement du nombre de soldat de mon unité 
if (nbsoldat-nb_mort>0){
nbsoldat= nbsoldat - nb_mort;}
else {nbsoldat = 0;}


 }



int main(){
    cout<<"welcome"<<endl;
    unity fantassin_leger_1(fantassin_leger, "1");
    unity fantassin_leger_2(fantassin_leger, "2");
  //  fantassin_leger_1.afficher();
 //fantassin_leger_2.afficher();
 //fantassin_leger_2.afficher_datasheet();

fantassin_leger_1.setnbsoldat(1);
//fantassin_leger_1.afficher();
 /*fantassin_leger_1.fight_unity_one_each_other(fantassin_leger_2,0, sans_protection,sans_protection);

     fantassin_leger_1.afficher();
 fantassin_leger_2.afficher();   
*/
//fantassin_leger_1.attacked_by_unit2(fantassin_leger_2,0,sans_protection);

  //   fantassin_leger_1.afficher();
 //fantassin_leger_2.afficher();   */

fantassin_leger_1.setnbsoldat(6);

//pb avec le trick de modifier le second fantassin
//int a=fantassin_leger_1.fight_unity_one_each_other(fantassin_leger_2,0, sans_protection,sans_protection);
//fantassin_leger_2.setnbsoldat(a);


 //fantassin_leger_1.afficher();
 //fantassin_leger_2.afficher();
unity fantassin_lourd_1(fantassin_lourd, "1");
unity canon_leger_1(canon_leger, "1");
unity canon_lourd_1(canon_lourd, "1");
unity char_leger_1(char_leger, "1");
unity char_lourd_1(char_lourd, "1");
/*
fantassin_lourd_1.afficher();
 canon_leger_1.afficher();
 canon_lourd_1.afficher();
char_leger_1.afficher();
 char_lourd_1.afficher();
*//*
cout <<frand_a_b(0,12 ) <<endl ;
cout <<frand_a_b(0,12 ) <<endl ;
cout <<frand_a_b(0,12 ) <<endl ;
cout <<frand_a_b(0,12 ) <<endl ;
cout <<frand_a_b(0,12 ) <<endl ;
*/
alea ();
    return 0;}