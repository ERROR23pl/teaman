import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SignupComponent } from './authentication/signup-form/signup.component';
import { SigninComponent } from './authentication/signin/signin.component';
import {WelcomeScreenComponent} from './authentication/welcome-screen/welcome-screen.component';
import {HomeHubComponent} from './home/home-hub/home-hub.component';
import {PageNotFoundComponent} from './page-not-found/page-not-found.component';


let default_route = WelcomeScreenComponent
export const routes: Routes = [
  { path: 'welcome-page', component: WelcomeScreenComponent },
  { path: 'home', component: HomeHubComponent },
  {
    path: 'signing',
    children: [
      { path: 'sign-up', component: SignupComponent },
      { path: 'sign-in', component: SigninComponent },
      { path: '', redirectTo: 'sign-in', pathMatch: "full"}
    ]
  },
  { path: '', redirectTo: 'welcome-page', pathMatch: "full"},
  { path: '**', component: PageNotFoundComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
