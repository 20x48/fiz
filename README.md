# FIZ

[中文](https://github.com/20x48/fiz/blob/main/README_zh.md)

A utility use to convert HEX to (i've tried my best) *Human.Spellable.Words.*

## Feature

1. The encoded size is *even worse than octal*.
2. Dynamic output length.
3. But most importantly, **human spellable**!

Ignore the first two and don't save too much on your UI.

**NOTE:**
Although it has been tested against a wide range of inputs (with correct type),
but there is still no guarantee that nothing will go wrong.
Before the test of time, I can't be sure of anything.
In addition, you can catch them by `except fiz.FizError`.

## Install

    pip install fiz

## Usage

``` python
In [1]: from fiz import Fiz

In [2]: Fiz(b'some bytes...')
Out[2]: 'Dacyorrheumiesciendlichouquinzai.Rsmoochylith.D.'

In [3]: Fiz(b'custom joiner', '-')
Out[3]: 'Taideutidipladeepfold-Tsphycomb-Nuf-Re'
```

## Long Long Examples

```
--- 1 ---
In:  C7D2D5DBC1F8A3ACB4FDCBFBC8D5A3ACD4D9CFE0B7EA
Out: Ndfallbendol.Skwogmirinicksongymnadequeet.Dde.Mser.Npassu.Rggily.Mnchoce
--- 2 ---
In:  CED2CEAAC4E320B3AAD2BBC7FA20C8E7D3CECBBFB5C4C6F8CFA2
Out: Nkwoodlitzes.Mmhorichloanemid.Elsacksummox.Usallys.Ufan.T.Iflask.Pos.Foxshipfe
--- 3 ---
In:  CCE1B1CAD7DFB5A4C7E020BAE1C6C3CBAEC4AB20B7D6B1F0D2D1B9FDC7A7C7EF20CAAEC0EFC7EFD2B6BAEC20D6B4B1CABBADCCC4CEAABEFDC1F420CAB1B9E2C8E7C1F7CBAE20B5E3B5E3B0A7B3EE20BDF1CFA6BFD5D2D0D0A1C2A520BEB2BFB4BAD3B1DFBFDDC1F820C8D4BFC9BCFBBEFDB7F1
Out: Nuptigroizedly.Tls.Dwyershortfirs.Net.Dr.Pyeticshipinofoilershopped.Ifehol.Pbonedly.Islesplin.Aeohippro.Ddlieshit.Hemphysnowts.Fuz.Tl.Dulan.Ilts.Osspromemoiredackeersty.Hfoe.Sknessly.Ann.Abag.Tredoximoblershedhandybonehowleecelicerioleums.Auked.Cquopersabdacistabdosimumly.Mstrail.Ormidomy.Ilotumta.Cnotiza.Tapmongcourebreadnut.Cogwooleye.Fedomizil.Dl.Fnullbit.Bi
--- 4 ---
In:  D2FBB9FDD2BBD5B5D3EABAF3CCECC7E0B4C920D2B2B2BBCBE3C0B4B3D9
Out: Icwiserraghs.Ognescati.Mfuseesawis.Mrena.Aggeis.Shynesicaliburoo.Hods.Nff.Ainworl.Aec
--- 5 ---
In:  B1CBCAB1C1B520D4B8BAA3CAC4C9BDC3CB
Out: Himsas.Cl.Amagilanco.Mlittifocklied.Uebrecco.Aia
```