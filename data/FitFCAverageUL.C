#include <TGraph.h>
#include <TF1.h>
#include <TCanvas.h>

void FitFCAverageUL(char* filename)
{
   // Create a graph reading from a CSV file
   TGraph* gr = new TGraph(filename, "%lg %lg", ",");

   // Fit a square-root function in the range [10.,100.]
   TF1* sqrtfit = new TF1("sqrtfit", "[0]+[1]*sqrt(x)", 20., 100.);
   sqrtfit->SetParameter(0, 1.5);
   sqrtfit->SetParameter(1, 1.5);

   gr->Fit("sqrtfit");

   c1 = new TCanvas("c1", "Feldman-Cousins Average UL", 200, 100, 600, 600);
   gr->Draw();
}
