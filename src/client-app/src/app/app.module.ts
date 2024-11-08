import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {AppComponent} from './app.component';
import {SigninComponent} from './authentication/signin/signin.component';
import {HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';
import {BrowserModule} from '@angular/platform-browser';
import {AppRoutingModule} from './app.routes';

import { MatDialogModule } from '@angular/material/dialog';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    AppComponent,
    SigninComponent,
    HttpClientModule,
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    MatDialogModule
  ],
  providers: []
})
export class AppModule { }
