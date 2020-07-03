import {Injectable} from '@angular/core';

import {Hero} from '../../model/hero/hero';
import {HEROES} from '../../mock/mock-heroes';
import { MessageService } from '../message/message.service';

import { Observable, of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class HeroService {
  getHeroes(): Observable<Hero[]> {
    this.messageService.add('HeroService: fetched heroes');
    return of(HEROES);
  }
  getHero(id: number): Observable<Hero> {
    this.messageService.add(`HeroService: fetch hero id=${id}`);
    return of(HEROES.find(hero => hero.id === id));
  }

  constructor(public messageService: MessageService) {
  }
}
