import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {TopBarComponent} from "./top-bar/top-bar.component";
import {BodyComponent} from "./body/body.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, TopBarComponent, BodyComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
