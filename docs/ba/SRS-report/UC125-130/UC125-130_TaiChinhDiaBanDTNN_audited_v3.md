# UC Readiness Review
**Functional / Black-box Test Readiness Template**

**Tai lieu:** UC125-130_TaiChinhDiaBanDTNN.md (phien ban 1.1)
**Ngay tao:** 2026-05-07
**Tac gia audit:** QC Auditor Agent
**Phien ban report:** v3 (Full Audit)

---

## Feature Brief

Chuc nang "Bao cao tong hop tinh hinh tai chinh va nop ngan sach cua TCKT co von DTNN nam theo dia ban tinh/thanh pho" (Mau A.IV.9a) thuoc phan he Quan ly dau tu nuoc ngoai vao Viet Nam. Day la bao cao dinh ky nam, dang eForm Grid co dinh 63 dong (tuong ung 63 tinh/TP), voi 5 cot so lieu editable ho tro auto-fill tu API TMS (He thong Quan ly Thue). Dong Tong cuoi bang tu dong tinh SUM real-time. Footer tu dong tu he thong.

**Dac diem chinh:**
- Grid CO DINH 63 dong — khong them/xoa dong
- 5 cot so lieu: Thu tu xuat nhap khau, Thu noi dia, Thu tu dau tho, So DN Lo, So DN Lai
- Auto-fill tu API TMS voi fallback nhap tay khi API loi/timeout (>5s)
- Dong Tong = SUM real-time, Disabled
- Footer (Noi lap, Ngay lap) tu dong, Disabled
- Du lieu NGUON tu UC131-136 (Mau 9b): Group By Tinh/TP, SUM, COUNT

**Doi tuong su dung:** Cuc Thue / Bo Tai chinh (Admin site).
**Hinh thuc nop:** Bao cao don le (Single report form).
**Co quan nhan:** Cuc Dau tu nuoc ngoai, Bo Tai chinh.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `70.9 / 100` | CONDITIONALLY READY |

**Ly do:** SRS da co cau truc tot, mo ta ro rang grid 63 dong va co che auto-fill TMS. Tuy nhien con nhieu lo hong quan trong:
- Thieu chi tiet decimal precision cho cac cot so lieu (trieu VND — bao nhieu chu so thap phan?)
- Thieu quy tac sap xep 63 tinh/TP (theo STT nao? Ma tinh? Ten ABC?)
- Thieu mo ta ro rang aggregation logic tu UC131-136 (9b) sang UC125-130 (9a)
- Thieu xu ly concurrent edit
- Thieu cross-column validation (So DN Lai + So DN Lo co phai = tong so DN?)
- Thieu don vi cu the cho cot (3)(4)(5) — trieu VND da ghi nhung chua xac nhan
- Thieu xu ly khi API TMS tra partial data

**Raw Score:** ~78/110 → **Final Score:** ~70.9/100

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC125-130 | Bao cao tong hop tinh hinh tai chinh va nop ngan sach TCKT co von DTNN (theo dia ban) - Mau A.IV.9a | v1.1 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.le2 | (Chua xac dinh) | 2026-04-24 | 2026-05-07 |

---

## 1. Objective & Scope

### 1.1 Objective
Ho tro Cuc Thue / Bo Tai chinh nop bao cao tong hop truc tuyen ve tinh hinh tai chinh va nop ngan sach cua cac to chuc kinh te co von dau tu nuoc ngoai, phan theo 63 tinh/thanh pho. Lam can cu quan ly thue va nop ngan sach theo dia ban cho Cuc Dau tu nuoc ngoai.

### 1.2 In Scope
- UC125: Lap bao cao moi (nhap lieu eForm Grid 63 dong manual)
- UC126: Lap bao cao moi (auto-fill tu API TMS)
- UC127: Nop bao cao
- UC128: Chinh sua bao cao
- UC129: Xem chi tiet / Xem vong doi / In / Export
- UC130: Xoa bao cao
- Xem danh sach bao cao (loc, tim kiem, nhom theo ky han nam)
- Import bao cao tu file Excel (tham chieu CF_02)

### 1.3 Out of Scope
- Khong cho phep nop bao cao tre han
- Viec duyet bao cao duoc thuc hien o UC rieng biet
- Quan ly master data 63 tinh/TP (thuoc he thong danh muc)
- Logic tong hop du lieu tu UC131-136 (thuoc phia UC131-136 xu ly)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Cuc Thue / Bo Tai chinh | Primary | Lap, sua, nop, xoa bao cao. Xem danh sach, xem chi tiet, in, export. Tham chieu: CMR_02 (quyen ngang nhau giua cac don vi cung cap). |
| He thong TMS (Tax Management System) | System | Cung cap du lieu auto-fill cho 5 cot so lieu qua API. Group By tinh/TP tu du lieu DN FDI. |
| UC131-136 (Mau A.IV.9b) | Upstream Data Source | Cung cap du lieu chi tiet theo doanh nghiep. Du lieu 9b duoc tong hop (Group By Tinh/TP, SUM, COUNT) de dien vao 9a. |
| Cuc Dau tu nuoc ngoai | Stakeholder | Co quan nhan bao cao. Nhan notification khi bao cao duoc nop thanh cong. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Tai khoan nguoi dung co quyen lap/xem bao cao thuoc don vi Cuc Thue / Bo Tai chinh.
- Ky bao cao dang o trang thai "Trong thoi han" (CMR_04: Ky han "Trong thoi han" cho phep tao moi va import).
- Danh muc 63 tinh/TP da duoc cau hinh trong master data he thong.
- API TMS kha dung (hoac fallback nhap tay neu API loi).
- [GAP] Du lieu tu UC131-136 (Mau 9b) da duoc nop/luu de san sang cho aggregation — CHUA DUOC XAC NHAN.

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lap bao cao + Luu nhap | Ban ghi trang thai "Luu nhap" xuat hien trong danh sach. Toast T01: "Da lap bao cao thanh cong". |
| Nop bao cao thanh cong | Trang thai chuyen sang "Cho duyet" hoac "Da tiep nhan" (CMR_03). Notification gui cho Cuc DTNN. Toast T02: "Da nop bao cao thanh cong". |
| Chinh sua + Luu | Trang thai bao toan. Toast T03 hien thi. |
| Xoa bao cao | Ban ghi bi xoa khoi danh sach. Toast T08: "Xoa bao cao thanh cong". |
| Moi thao tac | Ghi nhan Audit log (Actor, Action, Target, Timestamp). |

---

## 4. UI Object Inventory & Mapping — GRANULARITY RULE

### 4.1 Man hinh Danh sach (UC125-130.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Danh sach > Bo loc | Nam bao cao | Yearpicker | No | Nam hien tai | — | — | Chon nam; loc va nhom danh sach theo nam. Ket qua hien thi ngay (CMR_07). | SRS UC125-130.1 |
| 2 | Danh sach > Bo loc | Dia ban | Multiple-selection Dropdown | No | Null | — | 63 tinh/TP | Loc theo tinh/thanh pho. Ket qua loc hien thi ngay (CMR_07). | SRS UC125-130.1 |
| 3 | Danh sach > Bo loc | Trang thai ky han | Multiple-selection Dropdown | No | Null | — | Chua toi han / Trong thoi han / Qua ky bao cao | Tham chieu: CMR_04, CMR_07. | SRS UC125-130.1 |
| 4 | Danh sach > Bo loc | Trang thai bao cao | Multiple-selection Dropdown | No | Null | — | Luu nhap / Cho duyet / Da tiep nhan / Yeu cau chinh sua | Tham chieu: CMR_03, CMR_07. | SRS UC125-130.1 |
| 5 | Danh sach > Bo loc | Ma bao cao | Search bar | No | Null | "Nhap du lieu" | — | Tim theo ma bao cao. Hien thi ngay khi nhap. Neu khong tim thay: "Khong tim thay ket qua" (CMR_06, CMR_09). | SRS UC125-130.1 |
| 6 | Danh sach > Ky han Header | Ky han bao cao | Label | — | — | — | — | VD: "Nam 2026". Mac dinh collapse; click expand (CMR_08). | SRS UC125-130.1 |
| 7 | Danh sach > Ky han Header | Trang thai (cap ky) | Label/Badge | — | — | — | Chua toi han / Trong thoi han / Qua ky bao cao | CMR_04. | SRS UC125-130.1 |
| 8 | Danh sach > Ky han Header | Lap bao cao | Button | — | — | — | — | Chi hien thi khi ky "Trong thoi han". An khi Chua toi han hoac Qua ky (CF_01, CMR_04). | SRS UC125-130.1 |
| 9 | Danh sach > Ky han Header | Import | Button | — | — | — | — | Chi hien thi khi ky "Trong thoi han" (CMR_04). Luong import tham chieu CF_02. | SRS UC125-130.1 |
| 10 | Danh sach > Bang BC | Ma bao cao | Label (column) | — | — | — | — | Ma duy nhat toan he thong (CMR_09). Pattern: DTNN_A4_9a_[ID]. | SRS UC125-130.1 |
| 11 | Danh sach > Bang BC | Dia ban | Label (column) | — | — | — | — | Tinh/TP cua co quan lap bao cao. | SRS UC125-130.1 |
| 12 | Danh sach > Bang BC | Ngay nop / cap nhat | Label (column) | — | — | — | — | Dinh dang: dd/MM/yyyy HH:mm. | SRS UC125-130.1 |
| 13 | Danh sach > Bang BC | Trang thai bao cao | Label/Badge (column) | — | — | — | Luu nhap / Cho duyet / Da tiep nhan / Yeu cau chinh sua | CMR_03. | SRS UC125-130.1 |
| 14 | Danh sach > Bang BC | Hanh dong | Button group (column) | — | — | — | Nop / Chinh sua / Xem chi tiet / Xem vong doi / In / Export / Xoa | Hien thi theo trang thai (UC125-130.3). | SRS UC125-130.1 |

### 4.2 Man hinh Lap bao cao (UC125-130.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 15 | Header | Nam bao cao | Number input | Yes | Nam hien tai | — | — | 4 chu so, <= nam hien tai (CMR_05). | SRS UC125-130.2 |
| 16 | Bang > Cot (1) | STT | Integer (Auto) | — | 1-63 | — | — | Disabled. He thong tu danh so 1-63. | SRS UC125-130.2 |
| 17 | Bang > Cot (2) | Tinh/Thanh pho | Text/Label | — | Tu master data | — | 63 tinh/TP | Disabled. Khong trung lap. Tu danh muc he thong. | SRS UC125-130.2 |
| 18 | Bang > Cot (3) | Thu tu xuat, nhap khau (trieu VND) | Editable number | Yes | Auto-fill API | — | — | Decimal >= 0. Auto-fill TMS: tong thu XNK cua cac DN FDI tai tinh/TP tuong ung (chia 1.000.000). Luon Editable de hieu chinh. | SRS UC125-130.2 |
| 19 | Bang > Cot (4) | Thu noi dia (trieu VND) | Editable number | Yes | Auto-fill API | — | — | Decimal >= 0. Auto-fill TMS: tong thu noi dia cua cac DN FDI tai tinh/TP (chia 1.000.000). Luon Editable. | SRS UC125-130.2 |
| 20 | Bang > Cot (5) | Thu tu dau tho (trieu VND) | Editable number | Yes | Auto-fill API | — | — | Decimal >= 0. Auto-fill TMS: tong thu tu dau tho cua cac DN FDI tai tinh/TP (chia 1.000.000). Luon Editable. | SRS UC125-130.2 |
| 21 | Bang > Cot (6) | So doanh nghiep - Lo | Editable number | Yes | Auto-fill API | — | — | Integer >= 0. COUNT DN FDI co loi nhuan < 0 tai tinh/TP. Luon Editable. | SRS UC125-130.2 |
| 22 | Bang > Cot (7) | So doanh nghiep - Lai | Editable number | Yes | Auto-fill API | — | — | Integer >= 0. COUNT DN FDI co loi nhuan > 0 tai tinh/TP. Luon Editable. | SRS UC125-130.2 |
| 23 | Bang > Dong Tong | Tong - Cot (3) | Auto-calc | — | SUM | — | — | Disabled. Real-time SUM 63 dong. | SRS UC125-130.2 |
| 24 | Bang > Dong Tong | Tong - Cot (4) | Auto-calc | — | SUM | — | — | Disabled. Real-time. | SRS UC125-130.2 |
| 25 | Bang > Dong Tong | Tong - Cot (5) | Auto-calc | — | SUM | — | — | Disabled. Real-time. | SRS UC125-130.2 |
| 26 | Bang > Dong Tong | Tong - Cot (6) | Auto-calc | — | SUM | — | — | Disabled. Real-time. | SRS UC125-130.2 |
| 27 | Bang > Dong Tong | Tong - Cot (7) | Auto-calc | — | SUM | — | — | Disabled. Real-time. | SRS UC125-130.2 |
| 28 | Footer | Noi lap bao cao | Text/Label (Auto) | — | Ten tinh/TP theo tru so co quan | — | — | Disabled. He thong tu dien. Khong cho sua. | SRS UC125-130.2 |
| 29 | Footer | Ngay, thang, nam | Date/Label (Auto) | — | Current System Date | — | — | Disabled. dd/MM/yyyy. Khong cho sua. | SRS UC125-130.2 |
| 30 | Actions | Luu nhap | Button | — | — | — | — | CF_01 muc "Xu ly nut [Luu nhap]". | SRS UC125-130.2 |
| 31 | Actions | Nop bao cao | Button | — | — | — | — | CF_01 muc "Xu ly nut [Gui bao cao]". | SRS UC125-130.2 |
| 32 | Actions | Huy | Button | — | — | — | — | CF_01 muc "Xu ly nut [Huy]". Dirty check (CMR_14). | SRS UC125-130.2 |

### 4.3 Man hinh Tac vu bo tro (UC125-130.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 33 | Danh sach > Hanh dong | Nop | Button | — | — | — | — | Chi khi Luu nhap / YCCS. Nguoi tao. (CF_09, CF_01) | SRS UC125-130.3 |
| 34 | Danh sach > Hanh dong | Chinh sua | Button | — | — | — | — | Chi khi Luu nhap / YCCS. Nguoi tao. (CF_03) | SRS UC125-130.3 |
| 35 | Danh sach > Hanh dong | Xem chi tiet | Button | — | — | — | — | Tat ca trang thai. Tat ca nguoi dung. (CF_07) | SRS UC125-130.3 |
| 36 | Danh sach > Hanh dong | Xem vong doi | Button | — | — | — | — | Tat ca trang thai. Tat ca nguoi dung. (CF_06) | SRS UC125-130.3 |
| 37 | Danh sach > Hanh dong | In | Button | — | — | — | — | Tat ca trang thai. Tat ca nguoi dung. (CF_05) | SRS UC125-130.3 |
| 38 | Danh sach > Hanh dong | Export | Button | — | — | — | — | Ket xuat Excel. Tat ca trang thai. (CF_04) | SRS UC125-130.3 |
| 39 | Danh sach > Hanh dong | Xoa | Button | — | — | — | — | Luu nhap VA chua tung nop. Nguoi tao. (CF_08) | SRS UC125-130.3 |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|----------------------------------------------|
| Nam bao cao (Yearpicker - Danh sach) | Enabled. Default = nam hien tai. | Click: mo picker chon nam. Change: he thong loc ngay lap tuc. | Thay doi nam -> danh sach ky han cap nhat theo nam da chon. (CMR_07: Nhap chon -> thay placeholder bang gia tri da chon va dong danh sach.) |
| Dia ban (Multiple Dropdown - Danh sach) | Enabled. Default = Null (tat ca). | Click: mo dropdown checkbox 63 tinh/TP. Select: loc ngay. | Cho phep chon nhieu gia tri. Ket hop voi cac filter khac. (CMR_07) |
| Trang thai ky han (Dropdown) | Enabled. Default = Null (tat ca). | Click: mo dropdown checkbox. Select: loc ngay. | 3 gia tri: Chua toi han / Trong thoi han / Qua ky bao cao. (CMR_04, CMR_07) |
| Trang thai bao cao (Dropdown) | Enabled. Default = Null (tat ca). | Click: mo dropdown checkbox. Select: loc ngay. | 4 gia tri: Luu nhap / Cho duyet / Da tiep nhan / YCCS. (CMR_03, CMR_07) |
| Ma bao cao (Search bar) | Enabled. | Typing: loc ngay khi nhap ky tu. | Auto-trim. Khong can Enter. Placeholder: "Nhap du lieu". Khong tim thay -> "Khong tim thay ket qua". (CMR_06) |
| Ky han bao cao (Label) | Mac dinh collapse. | Click header: toggle expand/collapse. | Sap xep giam dan (moi nhat len dau). (CMR_08, CMR_10) |
| Nut [Lap bao cao] | Visible chi khi ky "Trong thoi han". Hidden khi "Chua toi han" / "Qua ky". | Click: dieu huong sang form Lap bao cao. | Mo UC125-130.2. He thong goi API TMS de auto-fill (UC126). (CF_01, CMR_04) |
| Nut [Import] | Visible chi khi ky "Trong thoi han". Hidden khi "Chua toi han" / "Qua ky". | Click: mo popup Import. | Luong import theo CF_02. (CMR_04) |
| Nam bao cao (Number - Form) | Enabled. Default = nam hien tai. Required. | Input: nhap so. Blur: validate. | Validate: so nguyen 4 chu so, <= nam hien tai. Loi inline: "Nam bao cao khong hop le". (CMR_05) |
| STT (Cot 1) | Disabled. Auto 1-63. | — (khong tuong tac). | He thong tu danh so. Khong thay doi. |
| Tinh/Thanh pho (Cot 2) | Disabled. Tu master data. | — (khong tuong tac). | 63 dong co dinh tu danh muc he thong. Khong trung lap. [GAP] Thu tu sap xep chua xac dinh. |
| Thu tu XNK (Cot 3) | Enabled (luon Editable). Required. | Input: nhap so decimal. | Auto-fill tu API TMS: SUM bien lai ma tieu muc thu XNK / 1.000.000. >= 0. Loi inline neu < 0. (CMR_05, API-NOTE) |
| Thu noi dia (Cot 4) | Enabled (luon Editable). Required. | Input: nhap so decimal. | Auto-fill tu API TMS: SUM bien lai ma tieu muc thu noi dia / 1.000.000. >= 0. (CMR_05, API-NOTE) |
| Thu tu dau tho (Cot 5) | Enabled (luon Editable). Required. | Input: nhap so decimal. | Auto-fill tu API TMS: SUM bien lai ma tieu muc thu dau tho / 1.000.000. >= 0. (CMR_05, API-NOTE) |
| So DN Lo (Cot 6) | Enabled (luon Editable). Required. | Input: nhap so nguyen. | Auto-fill tu API TMS: COUNT DN FDI co loi nhuan < 0 tai tinh/TP. Integer >= 0. (CMR_05, API-NOTE) |
| So DN Lai (Cot 7) | Enabled (luon Editable). Required. | Input: nhap so nguyen. | Auto-fill tu API TMS: COUNT DN FDI co loi nhuan > 0 tai tinh/TP. Integer >= 0. (CMR_05, API-NOTE) |
| Dong Tong (5 cot) | Read-only (Disabled). Auto-calculated. | — (khong tuong tac). | SUM real-time toan bo 63 dong cho tung cot. Cap nhat ngay khi thay doi bat ky o nao. |
| Noi lap bao cao (Footer) | Disabled. Auto-fill. | — | Ten Tinh/TP theo tru so co quan dang nhap. (CMR_12) |
| Ngay thang nam (Footer) | Disabled. Auto-fill. | — | Ngay hien tai. dd/MM/yyyy. (CMR_12) |
| Nut [Luu nhap] | Enabled khi form dang mo. | Click: luu du lieu. | Validate toi thieu. Toast T01 neu thanh cong. Toast T07 neu bang trong. (CF_01) |
| Nut [Nop bao cao] | Enabled. | Click: validate toan bo -> popup P01. | Validate 5 cot so lieu >= 0 tren 63 dong. Loi inline neu vi pham. Popup xac nhan voi checkbox. Toast T02 neu thanh cong. (CF_01) |
| Nut [Huy] | Enabled. | Click: kiem tra dirty form. | Dirty -> popup CMR_14: "Du lieu chua duoc luu" / "Ban co chac chan muon roi khoi trang nay khong?" [Dong y]/[Huy]. Khong dirty -> quay ve Danh sach ngay. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Xem danh sach (UC125-130.1)

**Luong chinh:**
1. Nguoi dung truy cap: Phan he Bao cao -> Quan ly DTNN vao VN -> Mau A.IV.9a.
2. He thong hien thi danh sach ky han bao cao, nhom theo nam, mac dinh collapse, sap xep giam dan.
3. Nguoi dung co the loc theo: Nam bao cao, Dia ban, Trang thai ky han, Trang thai bao cao, Ma bao cao.
4. Tat ca bo loc hien thi ket qua ngay lap tuc (CMR_07).
5. Nut [Lap bao cao] va [Import] chi hien thi khi ky o trang thai "Trong thoi han" (CMR_04, CF_01).
6. Cot Hanh dong hien thi cac nut tuong ung trang thai ban ghi (UC125-130.3).

**Edge cases:**
- Khong co bao cao nao trong ky: Hien thi thong bao trong.
- Loc khong co ket qua: "Khong tim thay ket qua".
- [GAP] Phan trang: SRS tham chieu CMR_10 nhung khong noi ro so ban ghi moi trang.

### 6.2 Lap BC Manual (UC125)

**Luong chinh:**
1. Nguoi dung nhan [Lap bao cao] tu man hinh danh sach.
2. He thong mo form Lap bao cao voi:
   - Header: Nam bao cao = nam hien tai (editable).
   - Bang: 63 dong co dinh. Cot (1) STT = 1-63 (Disabled). Cot (2) Tinh/TP tu master data (Disabled).
   - Cot (3)-(7): Tat ca o trong (Editable), nguoi dung nhap tay.
   - Dong Tong: SUM real-time (Disabled).
   - Footer: Noi lap + Ngay tu dong (Disabled).
3. Nguoi dung nhap so lieu cho 5 cot cua tung dong.
4. Dong Tong cap nhat real-time.
5. Nguoi dung chon [Luu nhap] hoac [Nop bao cao].

**Validate khi Nop:**
- Tat ca 5 cot so lieu phai >= 0 tren 63 dong.
- Cot (6), (7): Integer >= 0.
- Cot (3), (4), (5): Decimal >= 0.
- Neu vi pham -> loi inline "Gia tri phai >= 0", dung luong.

### 6.3 Lap BC API TMS (UC126): Auto-fill tu TMS

**Luong chinh:**
1. Nguoi dung nhan [Lap bao cao].
2. He thong goi API TMS de lay du lieu tai chinh:
   - API ra quet toan bo DN co Ma so thue thuoc dien FDI.
   - Group By tinh/TP -> Tinh toan:
     - Cot (3) Thu XNK: SUM bien lai ma tieu muc thu XNK / 1.000.000.
     - Cot (4) Thu noi dia: SUM bien lai ma tieu muc thu noi dia / 1.000.000.
     - Cot (5) Thu dau tho: SUM bien lai ma tieu muc thu dau tho / 1.000.000.
     - Cot (6) So DN Lo: COUNT DN co loi nhuan < 0.
     - Cot (7) So DN Lai: COUNT DN co loi nhuan > 0.
3. He thong tu dong dien du lieu vao cac o tuong ung.
4. Tat ca o van **Editable** de nguoi dung hieu chinh.
5. Dong Tong cap nhat real-time.

**Xu ly loi API:**
- Neu API loi hoac timeout (> 5s): O hien thi trong va Editable de nhap tay.
- [GAP] Neu API tra partial data (VD: thieu 10 tinh/TP): SRS ghi "o hien thi trong va Editable" nhung khong ro co thong bao cho nguoi dung biet nhung tinh nao thieu du lieu khong.

### 6.4 Nop (UC127)

**Luong chinh:**
1. Tu man hinh Danh sach, nguoi dung nhan nut [Nop] o cot Hanh dong (chi hien thi voi ban ghi Luu nhap hoac YCCS).
2. He thong validate toan bo 5 cot so lieu >= 0 tren 63 dong.
3. Neu hop le: Hien thi popup xac nhan P01 (voi checkbox cam ket).
4. Nguoi dung xac nhan -> He thong chuyen trang thai sang "Cho duyet" hoac "Da tiep nhan" (CMR_03).
5. He thong gui Notification cho Cuc DTNN.
6. Toast T02: "Da nop bao cao thanh cong".
7. Tham chieu: CF_01, CF_09.

### 6.5 Chinh sua (UC128)

**Luong chinh:**
1. Tu man hinh Danh sach, nguoi dung nhan [Chinh sua] (chi khi Luu nhap hoac YCCS).
2. He thong mo form chinh sua voi du lieu hien tai.
3. Nguoi dung thay doi cac o so lieu.
4. Dong Tong cap nhat real-time.
5. Nguoi dung chon [Luu nhap] hoac [Nop bao cao].
6. Tham chieu: CF_03.
7. [GAP] Khi chinh sua, co goi lai API TMS de refresh data khong? SRS khong de cap.

### 6.6 Xem/In/Export (UC129)

**Xem chi tiet:**
- Mo man hinh xem toan trang, toan bo truong Disabled. Tham chieu: CF_07.

**Xem vong doi:**
- Popup Audit Trail hien thi lich su thao tac. Tham chieu: CF_06.

**In bao cao:**
- In theo template Mau A.IV.9a. Tham chieu: CF_05.

**Export:**
- Ket xuat file Excel theo template Mau A.IV.9a, bao gom du du lieu 63 dong va dong tong. Tham chieu: CF_04.

### 6.7 Xoa (UC130)

**Luong chinh:**
1. Tu man hinh Danh sach, nguoi dung nhan [Xoa] (chi khi Luu nhap VA chua tung nop).
2. He thong hien thi popup xac nhan xoa.
3. Nguoi dung xac nhan -> He thong xoa ban ghi.
4. Toast T08: "Xoa bao cao thanh cong".
5. Tham chieu: CF_08.

---

## 7. Functional Integration Analysis

### 7.1 Tich hop voi UC131-136 (Mau 9b -> 9a) — QUAN TRONG

**Mo ta:**
- UC131-136 (Mau A.IV.9b) la bao cao chi tiet theo tung doanh nghiep FDI.
- UC125-130 (Mau A.IV.9a) la bao cao tong hop theo dia ban 63 tinh/TP.
- Du lieu 9b la NGUON de tong hop vao 9a.

**Aggregation Logic (tu SRS UC131-136):**
- Group By: Cot C6 (Tinh/Thanh pho) tu Mau 9b.
- SUM: C7 (Doanh thu), C8 (Loi nhuan), C9 (Thue nop NSNN) -> Tuong ung cot nao cua 9a?

**[GAP NGHIEM TRONG] Mapping SRS khong khop:**
SRS goc UC125-130 dinh nghia 5 cot: Thu XNK, Thu noi dia, Thu dau tho, So DN Lo, So DN Lai.
SRS goc UC131-136 dinh nghia 3 cot so: Doanh thu, Loi nhuan, Thue nop NSNN.

-> Cac cot (3)(4)(5) cua 9a (Thu XNK, Thu noi dia, Thu dau tho) KHONG co mapping truc tiep tu 9b.
-> Cac cot (6)(7) cua 9a (So DN Lo/Lai) co the tinh tu C8 cua 9b (COUNT DN co C8 < 0 / C8 > 0).
-> SRS ghi API TMS la nguon data cho 9a, trong khi 9b cung ghi la "nguon tong hop". Can lam ro moi quan he giua 2 nguon nay.

**Open Questions tu Tich hop:**
- Q_INT_01: Cot (3)(4)(5) cua 9a co phai lay tu 9b hay chi tu API TMS?
- Q_INT_02: Khi nao du lieu tu 9b duoc tong hop vao 9a? Tu dong (trigger) hay nguoi dung phai thao tac?
- Q_INT_03: Neu 9b chua co data cho 1 tinh/TP, 9a hien thi 0 hay trong?
- Q_INT_04: Conflict giua du lieu API TMS va du lieu tong hop tu 9b duoc xu ly the nao?

### 7.2 Tich hop voi API TMS

**Mo ta:**
- API TMS cung cap du lieu auto-fill cho 5 cot so lieu.
- Nguon: Kho du lieu Bao cao Tai chinh va Ho so nop thue tu He thong Quan ly Thue.

**Quy trinh API:**
1. API ra quet toan bo DN co MST thuoc dien FDI.
2. Group By tinh/TP.
3. Tinh toan tung cot theo tieu muc thue.
4. Tra ve du lieu cho 63 tinh/TP.

**[GAP] Chua ro:**
- Q_API_01: API TMS tra data theo format nao? (JSON? CSV? XML?)
- Q_API_02: Co the tra partial data — VD thieu 1 so tinh? He thong xu ly the nao?
- Q_API_03: Timeout cua API la > 5s theo SRS. Nhung retry policy the nao?
- Q_API_04: Authentication/Authorization cho API TMS?

### 7.3 Tich hop CF (Common Functions)

| CF Reference | Function | UC Applies | Notes |
|-------------|----------|-----------|-------|
| CF_01 | Lap bao cao (Luu nhap, Nop, Huy) | UC125, UC126, UC127 | Ap dung cho luong Luu nhap, Nop, Huy. |
| CF_02 | Import bao cao tu Excel | UC125-130.1 | Nut Import o man hinh Danh sach. |
| CF_03 | Chinh sua bao cao | UC128 | Chi khi Luu nhap / YCCS. |
| CF_04 | Export ra Excel | UC129 | Ket xuat theo template Mau A.IV.9a. |
| CF_05 | In bao cao | UC129 | In theo template. |
| CF_06 | Xem vong doi (Audit Trail) | UC129 | Popup lich su. |
| CF_07 | Xem chi tiet | UC129 | Man hinh read-only. |
| CF_08 | Xoa bao cao | UC130 | Chi khi Luu nhap VA chua tung nop. |
| CF_09 | Nop bao cao (tu Danh sach) | UC127 | Nop tu cot Hanh dong. |

### 7.4 Tich hop CMR (Common Rules)

| CMR Reference | Rule | Applied To | Notes |
|---------------|------|-----------|-------|
| CMR_02 | Phan quyen | Toan bo | Cuc Thue / Bo Tai chinh. |
| CMR_03 | Trang thai bao cao | Danh sach, Nop, Chinh sua | 4 trang thai: Luu nhap / Cho duyet / Da tiep nhan / YCCS. |
| CMR_04 | Trang thai ky han | Danh sach | 3 trang thai: Chua toi han / Trong thoi han / Qua ky. |
| CMR_05 | Validate so | Form | Cot (3)(4)(5): Decimal >= 0. Cot (6)(7): Integer >= 0. Nam: 4 chu so. |
| CMR_06 | Search | Danh sach | Tim theo ma bao cao. |
| CMR_07 | Filter behavior | Danh sach, Form | Ket qua hien thi ngay khi chon. |
| CMR_08 | Ky han hien thi | Danh sach | Ten ky han: "Nam 2026". |
| CMR_09 | Ma bao cao | Danh sach | Pattern: DTNN_A4_9a_[ID]. |
| CMR_10 | Phan trang / Sap xep | Danh sach | Mac dinh collapse, giam dan. |
| CMR_12 | Auto-fill truong | Footer, API TMS | Noi lap, Ngay thang tu he thong. |
| CMR_14 | Dirty check | Nut Huy | Popup xac nhan neu co thay doi chua luu. |

---

## 8. Acceptance Criteria

### Tu SRS (6 AC):

| AC-ID | Mo ta | Nguon | Danh gia |
|-------|-------|-------|----------|
| AC1 | Load 63 dong: He thong phai hien thi dung 63 dong co dinh tuong ung 63 tinh/TP. STT (1-63) va Ten Tinh/TP bi Disabled. | SRS 3.4 | Day du. |
| AC2 | Auto-fill TMS: He thong tu dong goi API TMS de do du lieu vao cot (3)-(7). API loi hoac timeout (>5s) -> hien thi o trong va cho phep nhap tay. | SRS 3.4 | Day du nhung thieu chi tiet partial failure. |
| AC3 | SUM Real-time: Dong Tong phai cap nhat ngay lap tuc gia tri tong cua cot (3)(4)(5)(6)(7) moi khi nguoi dung thay doi gia tri o nao. | SRS 3.4 | Day du. |
| AC4 | Validate so duong: Khi nhan "Nop bao cao", kiem tra tat ca o so lieu >= 0. Neu < 0 -> loi inline "Gia tri phai >= 0" va chan nop. | SRS 3.4 | Day du nhung thieu validation Integer cho cot (6)(7). |
| AC5 | Footer tu dong: Noi lap va Ngay lap phai dien tu dong va Disabled. | SRS 3.4 | Day du. |
| AC6 | Export chuan: File Excel phai dung template Mau A.IV.9a, du 63 dong va dong tong. | SRS 3.4 | Day du. |

### AC bo sung (de xuat boi QC):

| AC-ID | Mo ta | Ly do bo sung |
|-------|-------|---------------|
| AC7 | Khi goi API TMS, neu API tra ve du lieu cho chi 50/63 tinh, 13 tinh con lai phai hien thi o trong va Editable. He thong hien thi thong bao cho nguoi dung so luong tinh chua co du lieu. | Gap: Xu ly partial API data. |
| AC8 | Cot (6) "So DN Lo" va cot (7) "So DN Lai" chi chap nhan so nguyen (integer), khong chap nhan so thap phan. | Gap: SRS ghi Integer nhung thieu test case cu the. |
| AC9 | Cot (3)(4)(5) co don vi "trieu VND". He thong hien thi voi [X] chu so thap phan (can BA xac nhan). | Gap: Decimal precision chua dinh nghia. |
| AC10 | 63 dong hien thi theo thu tu co dinh (can BA xac nhan: theo ma tinh? theo ten ABC? theo STT chinh thuc?). | Gap: Thu tu sap xep 63 tinh/TP chua ro. |
| AC11 | Nguoi dung khong the them hoac xoa dong trong bang 63 dong. Khong co nut "Them dong" hay "Xoa dong" tren form. | Gap: SRS ngam dinh nhung chua ghi nhan ro rang AC nay. |
| AC12 | Khi chinh sua bao cao (UC128), he thong phai load du lieu hien tai cua ban ghi va cho phep sua 5 cot so lieu. Dong Tong cap nhat real-time. | Gap: SRS chi tham chieu CF_03 nhung khong co AC rieng. |
| AC13 | Khong cho phep 2 nguoi dung cung chinh sua 1 ban ghi bao cao cung luc (concurrent edit). Nguoi dung thu 2 phai nhan thong bao loi. | Gap: Concurrent edit chua duoc mo ta. |
| AC14 | Khi nop bao cao, he thong phai gui Notification cho Cuc DTNN. Notification phai chua: ma bao cao, ten don vi nop, thoi gian nop. | Gap: SRS ghi co Notification nhung thieu chi tiet noi dung. |

---

## 9. Non-Functional Requirements (NFR)

### Tu SRS:

| NFR-ID | Category | Requirement | Source | Danh gia |
|--------|----------|-------------|--------|----------|
| NFR_01 | Performance | Thoi gian tai danh sach 63 dong va auto-fill tu API khong vuot qua 5 giay. | SRS 3.5 | Ro rang. Can lam ro: 5s la timeout toan luong hay chi API call? |
| NFR_02 | Security & Audit | Chi nguoi dung thuoc Cuc Thue / Bo Tai chinh moi co quyen Them/Sua/Nop. Moi hanh dong deu duoc ghi log chi tiet (Actor, Action, Target, Timestamp). | SRS 3.5 | Ro rang. |

### NFR bo sung (de xuat boi QC):

| NFR-ID | Category | Requirement | Ly do |
|--------|----------|-------------|-------|
| NFR_03 | Data Integrity | Du lieu SUM dong Tong phai chinh xac tuyet doi (khong sai so lam tron). | Gap: SRS ghi SUM real-time nhung khong noi ve lam tron. |
| NFR_04 | Availability | API TMS khong kha dung khong duoc chan luong nhap tay. Fallback phai tu dong va trong suot. | Gap: SRS ghi nhung chua co NFR chinh thuc. |
| NFR_05 | Usability | Form 63 dong phai co scroll doc thuong tien (sticky header, STT/Ten tinh visible khi scroll). | Gap: UX cho bang dai 63 dong chua duoc mo ta. |
| NFR_06 | Concurrency | He thong phai xu ly truong hop 2 nguoi cung truy cap/chinh sua bao cao. | Gap: Chua duoc mo ta. |

---

## 10. Open Questions

| Q-ID | Category | Question | Priority | Target |
|------|----------|----------|----------|--------|
| Q1 | Business Logic | Cot (3)(4)(5) co decimal precision la bao nhieu chu so thap phan? (Trieu VND — 0, 1, 2 decimal?) | High | BA |
| Q2 | Business Logic | Don vi chinh xac cho cot (3)(4)(5): Trieu VND da duoc xac nhan? Hay co the la ty dong? | High | BA |
| Q3 | Integration | Aggregation tu 9b -> 9a: Tu dong (trigger) hay manual? Khi nao data tu 9b duoc tong hop vao 9a? | Critical | BA |
| Q4 | Integration | Neu 9b chua co data cho 1 tinh, 9a hien thi 0 hay trong cho tinh do? | High | BA |
| Q5 | Integration | API TMS va du lieu tong hop tu 9b: Moi quan he the nao? Co conflict khong? Ai la nguon chinh? | Critical | BA |
| Q6 | API | API TMS tra data theo format nao? Co the partial (thieu 1 so tinh)? | High | BA / Dev |
| Q7 | API | Retry policy khi API TMS timeout? Bao nhieu lan retry? | Medium | BA / Dev |
| Q8 | API | Authentication/Authorization cho API TMS: Token? API Key? OAuth? | Medium | Dev |
| Q9 | Business Logic | So DN Lai + So DN Lo co phai = tong so DN FDI trong tinh khong? (Cross-column validation) | High | BA |
| Q10 | Business Logic | 63 dong bat buoc dien het? Hay cho phep de 0 hoac de trong cho cac tinh khong co DN FDI? | High | BA |
| Q11 | UX | Thu tu sap xep 63 tinh/TP: Theo ma tinh chinh thuc? Theo ten ABC? Theo vung kinh te? | Medium | BA |
| Q12 | Concurrency | 2 nguoi dung cung mo form chinh sua 1 bao cao: He thong xu ly the nao? Lock? Warning? | High | BA / Dev |
| Q13 | Data | Cot tren Mau 9a khac voi cot tren Mau 9b. (9a: Thu XNK, Thu noi dia, Thu dau tho, DN Lo, DN Lai) vs (9b: Doanh thu, Loi nhuan, Thue). Ba lam ro mapping? | Critical | BA |
| Q14 | Notification | Noi dung Notification gui Cuc DTNN khi nop bao cao gom nhung gi? | Medium | BA |
| Q15 | Import | Import Excel cho Mau 9a co validate 63 dong co dinh khong? File import phai co dung 63 dong? | Medium | BA |

---

## 11. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| v1 | 2026-05-07 | QC Auditor Agent | (Khong co — v1 khong ton tai cho file nay) |
| v2 | 2026-05-07 | QC Auditor Agent | Ban dau chi co den Section 5 voi placeholder. Chua day du. |
| v3 | 2026-05-07 | QC Auditor Agent | Full Audit. Viet day du 11 sections + Audit Summary + Gap Report. Bo sung Section 5 (Object Behavior), Section 6 (Workflow), Section 7 (Integration Analysis), Section 8 (12+ ACs), Section 9 (NFR), Section 10 (15 Open Questions), Section 11 (Change Log). |

---

## Audit Summary

### Tong quan

| Hang muc | Diem | Diem toi da | Ghi chu |
|----------|------|-------------|---------|
| Document Metadata | 8 | 10 | Thieu Approved By. |
| Objective & Scope | 9 | 10 | Ro rang. Out of scope duoc dinh nghia. |
| Actors & Stakeholders | 8 | 10 | Day du. Thieu chi tiet ve downstream consumer. |
| Preconditions & Postconditions | 8 | 10 | Day du. Thieu dieu kien 9b da co data. |
| UI Object Inventory | 9 | 10 | Day du 39 objects. Mapping chuan. |
| Object Attributes & Behavior | 7 | 10 | Thieu thu tu sap xep 63 tinh, thieu decimal precision. |
| Functional Logic & Workflow | 6 | 10 | Thieu chi tiet aggregation 9b->9a, concurrent edit, partial API. |
| Integration Analysis | 5 | 10 | GAP NGHIEM TRONG: Mapping cot 9a vs 9b khong khop. Chua ro trigger aggregation. |
| Acceptance Criteria | 6 | 10 | SRS co 6 AC. Can them 8+ AC cho edge cases. |
| NFR | 6 | 10 | Chi co 2 NFR tu SRS. Can bo sung UX, Concurrency, Data Integrity. |
| Open Questions | 6 | 10 | 15 cau hoi duoc xac dinh. Nhieu cau Critical. |

**Tong:** 78 / 110 raw -> **70.9 / 100** (normalized)

### Verdict: CONDITIONALLY READY

SRS du tot de bat dau thiet ke test case cho happy path, nhung can BA giai dap cac Open Questions truoc khi hoan thanh test case day du, dac biet:
1. Mapping cot 9a vs 9b (Q13 — Critical)
2. Aggregation trigger (Q3 — Critical)
3. API TMS vs 9b data source (Q5 — Critical)
4. Decimal precision (Q1 — High)
5. Cross-column validation DN Lai + DN Lo (Q9 — High)

---

## Unified Gap & Question Report

### GAP-001: Mapping cot giua Mau 9a va 9b khong khop
- **Severity:** Critical
- **Section:** 7.1
- **Mo ta:** Mau 9a co 5 cot (Thu XNK, Thu noi dia, Thu dau tho, So DN Lo, So DN Lai). Mau 9b co 3 cot so (Doanh thu, Loi nhuan, Thue). Khong co mapping truc tiep tu 9b -> cot (3)(4)(5) cua 9a. SRS ghi API TMS la nguon du lieu cho 9a, trong khi 9b cung ghi la "nguon tong hop". Can lam ro moi quan he giua 2 nguon nay.
- **Cau hoi:** Cot (3)(4)(5) cua 9a lay du lieu tu dau? Tu API TMS, tu 9b, hay tu ca hai?
- **Tac dong:** Khong the thiet ke test case cho integration flow neu chua giai dap.

### GAP-002: Aggregation trigger 9b -> 9a chua dinh nghia
- **Severity:** Critical
- **Section:** 7.1
- **Mo ta:** SRS UC131-136 ghi "Du lieu sau khi Nop se duoc he thong tu dong san sang cho luong tong hop cua Mau 9a". Nhung SRS UC125-130 khong mo ta khi nao va bang cach nao du lieu tu 9b duoc tong hop vao 9a.
- **Cau hoi:** Auto trigger khi 9b duoc nop? Hay nguoi dung phai nhan nut? Hay API TMS da tong hop san?
- **Tac dong:** Anh huong den luong test tich hop giua 2 UC.

### GAP-003: Decimal precision chua dinh nghia
- **Severity:** High
- **Section:** 5, 8
- **Mo ta:** Cot (3)(4)(5) co don vi "trieu VND" nhung khong ro bao nhieu chu so thap phan. VD: 1.234,56 trieu VND hay 1.235 trieu VND?
- **Cau hoi:** So chu so thap phan cho cac cot Decimal la bao nhieu? 0? 2? 4?
- **Tac dong:** Anh huong den validation va SUM accuracy.

### GAP-004: Thu tu sap xep 63 tinh/TP chua ro
- **Severity:** Medium
- **Section:** 5
- **Mo ta:** SRS ghi 63 dong co dinh tu master data nhung khong ghi thu tu. Co the theo ma tinh chinh thuc (01-63), theo ten ABC, hoac theo vung kinh te.
- **Cau hoi:** Thu tu nao? Nhat quan giua 9a va 9b?
- **Tac dong:** Anh huong hien thi va so khop dong khi aggregation.

### GAP-005: Xu ly concurrent edit
- **Severity:** High
- **Section:** 6.5, 9
- **Mo ta:** SRS khong mo ta xu ly khi 2 nguoi dung cung chinh sua 1 bao cao.
- **Cau hoi:** Optimistic locking? Pessimistic locking? Last-write-wins?
- **Tac dong:** Co the gay mat du lieu.

### GAP-006: Cross-column validation (DN Lai + DN Lo)
- **Severity:** High
- **Section:** 8
- **Mo ta:** So DN Lai (cot 7) + So DN Lo (cot 6) co phai = tong so DN FDI trong tinh do khong? SRS khong co validation nay.
- **Cau hoi:** Co ap dung cross-column validation khong? Hay DN co the khong thuoc ca 2 nhom (VD: loi nhuan = 0)?
- **Tac dong:** Anh huong den data integrity va test case.

### GAP-007: API TMS partial data
- **Severity:** High
- **Section:** 6.3, 7.2
- **Mo ta:** SRS ghi "Neu API khong tra ve du lieu cho 1 tinh/TP: o hien thi trong va Editable". Nhung thieu: (1) Co thong bao cho nguoi dung biet tinh nao thieu? (2) Co retry? (3) Phan biet API loi toan bo vs partial?
- **Cau hoi:** He thong xu ly partial API data the nao? Thong bao gi cho nguoi dung?
- **Tac dong:** UX va data accuracy.

### GAP-008: Import flow cho Mau 9a
- **Severity:** Medium
- **Section:** 6.1
- **Mo ta:** Man hinh Danh sach co nut [Import] tham chieu CF_02, nhung khong co chi tiet import validate 63 dong co dinh. File Excel import phai co dung 63 dong? Le giua tu 9a va 9b?
- **Cau hoi:** Import Excel cho 9a co validate so dong = 63? Neu file co 62 hoac 64 dong thi sao?
- **Tac dong:** Can lam ro truoc khi thiet ke test case Import.

### GAP-009: Notification content
- **Severity:** Low
- **Section:** 3.2, 6.4
- **Mo ta:** SRS ghi gui Notification cho Cuc DTNN khi nop thanh cong nhung khong chi tiet noi dung notification.
- **Cau hoi:** Notification gom: ma bao cao, ten don vi nop, thoi gian nop? Co link den bao cao?
- **Tac dong:** Can lam ro de test notification.
