import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SignupComponent } from './signup/signup-form/signup.component';
import { SigninComponent } from './signin/signin.component';


let default_route = SigninComponent
export const routes: Routes = [
  { path: '', component: default_route },
  { path: 'sign-up', component: SignupComponent },
  { path: 'sign-in', component: SigninComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
