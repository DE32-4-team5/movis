package com.samdul.movis.entity;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Setter
@Getter
@ToString
public class MovisEntity {
    private Integer movieCd;
    private String movieNm;
    private String movieNmEn;
    private String openDt;
    private String repGenreNm;
    private String repNationNm;
    private String peopleNm;

}
